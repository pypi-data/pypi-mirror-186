# -*- coding: utf-8 -*-
import datetime
import re

from rest_framework import (
    filters,
    mixins,
    permissions,
    serializers,
    status,
    viewsets,
)
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet, ReadOnlyModelViewSet

from django.db.models import Q, Count, BooleanField
from django.db.models.functions import Cast
from django_filters.rest_framework import DjangoFilterBackend

from notifications.models import (
    UserDevice,
    UserNotification,
    Notification,
    Topic,
)
from notifications.push.settings import SETTINGS

from .permissions import IsOwner
from .serializers import (
    DeviceSerializer,
    TopicSerializer,
    UserNotificationSerializer,
    UserNotificationPutSerializer,
    NotificationSerializer,
)


class UserNotificationViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = UserNotification.objects.all()

    permission_classes = (permissions.IsAuthenticated,)

    filter_backends = (filters.SearchFilter, DjangoFilterBackend)

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            serializer_class = UserNotificationPutSerializer
        else:
            serializer_class = UserNotificationSerializer
        return serializer_class

    def list(self, request):
        queryset = self.queryset.filter(
            Q(user=self.request.user) &
            (Q(next_display__isnull=True) | Q(next_display__lte=datetime.datetime.now())) &
            (Q(notification__expires__isnull=True) | Q(notification__expires__gte=datetime.datetime.now())) &
            (Q(notification__active_from__isnull=True) | Q(notification__active_from__lt=datetime.datetime.now()))
        ).exclude(answer=True).select_related('notification', 'user').order_by('timestamp', 'id')
        path = request.query_params.get('path', None)
        if path is not None:
            queryset = [
                un for un in queryset
                if re.match(un.notification.display_only_if_url_path_matches_regex, path) is not None
            ]
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if instance.user != request.user:
            raise serializers.ValidationError('User can only change his own usernotifications')
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class NotificationViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Notification.objects.all()

    permission_classes = (permissions.IsAdminUser,)
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)

    serializer_class = NotificationSerializer

    def list(self, request):
        queryset = Notification.objects.filter()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Mixins
class DeviceViewSetMixin:
    lookup_field = "registration_id"

    def create(self, request, *args, **kwargs):
        serializer = None
        is_update = False
        if (
            SETTINGS.get("UPDATE_ON_DUPLICATE_REG_ID")
            and "registration_id" in request.data
        ):
            instance = self.queryset.model.objects.filter(
                registration_id=request.data["registration_id"]
            ).first()
            if instance:
                serializer = self.get_serializer(instance, data=request.data)
                is_update = True
        if not serializer:
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        if is_update:
            self.perform_update(serializer)
            return Response(serializer.data)
        else:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            if SETTINGS["ONE_DEVICE_PER_USER"] and self.request.data.get(
                "active", True
            ):
                UserDevice.objects.filter(
                    user=self.request.user).update(active=False)
            return serializer.save(user=self.request.user)
        return serializer.save()

    def perform_update(self, serializer):
        if self.request.user.is_authenticated:
            if SETTINGS["ONE_DEVICE_PER_USER"] and self.request.data.get(
                "active", False
            ):
                UserDevice.objects.filter(
                    user=self.request.user).update(active=False)

            return serializer.save(user=self.request.user)
        return serializer.save()


class AuthorizedMixin:
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def get_queryset(self):
        # filter all devices to only those belonging to the current user
        return self.queryset.filter(user=self.request.user)


# ViewSets
class DeviceViewSet(DeviceViewSetMixin, ModelViewSet):
    queryset = UserDevice.objects.order_by("-id")
    serializer_class = DeviceSerializer


class DeviceCreateOnlyViewSet(DeviceViewSetMixin, CreateModelMixin, GenericViewSet):
    queryset = UserDevice.objects.all()
    serializer_class = DeviceSerializer


class DeviceAuthorizedViewSet(AuthorizedMixin, DeviceViewSet):
    pass


class TopicViewSet(ReadOnlyModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        qs = super().get_queryset()
        subscribed = Cast(
            Count('subscribers', filter=Q(subscribers=self.request.user)),
            output_field=BooleanField()
        )
        return qs.annotate(subscribed=subscribed)

    @action(methods=['post'], detail=True)
    def subscribe(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.subscribers.add(request.user)
        setattr(obj, 'subscribed', True)
        data = self.serializer_class(instance=obj).data
        return Response(data, status=status.HTTP_201_CREATED)

    @action(methods=['post'], detail=True)
    def unsubscribe(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.subscribers.remove(request.user)
        setattr(obj, 'subscribed', False)
        data = self.serializer_class(instance=obj).data
        return Response(data, status=status.HTTP_201_CREATED)
