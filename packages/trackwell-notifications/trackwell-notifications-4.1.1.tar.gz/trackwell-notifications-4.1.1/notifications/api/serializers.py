# -*- coding: utf-8 -*-
from django.db.models import Q
from rest_framework.serializers import ModelSerializer, ValidationError
from rest_framework import serializers

from notifications.models import (
    UserDevice,
    Notification,
    Topic,
    UserNotification,
)


from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', )


class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    regex = serializers.CharField(source='display_only_if_url_path_matches_regex')
    class Meta:
        model = Notification
        fields = ('name', 'message', 'snooze_time', 'snooze_lock', 'look', 'image', 'regex',)


class UserNotificationSerializer(serializers.HyperlinkedModelSerializer):
    notification = NotificationSerializer()
    user = UserSerializer()

    class Meta:
        model = UserNotification
        fields = ('id', 'notification', 'user', 'seen', 'answer')


class UserNotificationPutSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserNotification
        fields = ('answer', 'answer_string')


class DeviceSerializer(ModelSerializer):
    # The origianl code for this serializer comes from the fcm-django module and is subject
    # to an MIT license. We may have modified the code from the original source to fit our needs.
    # For original source see: https://github.com/xtrinch/fcm-django
    class Meta:
        model = UserDevice
        fields = (
            "id",
            "name",
            "registration_id",
            "device_id",
            "active",
            "date_created",
            "type",
        )
        read_only_fields = ("date_created",)
        extra_kwargs = {"active": {"default": True}, "id": {"read_only": True, "required": False}}

    def validate(self, attrs):
        devices = None
        primary_key = None
        request_method = None

        if self.initial_data.get("registration_id", None):
            if self.instance:
                request_method = "update"
                primary_key = self.instance.id
            else:
                request_method = "create"
        else:
            if self.context["request"].method in ["PUT", "PATCH"]:
                request_method = "update"
                primary_key = self.instance.id
            elif self.context["request"].method == "POST":
                request_method = "create"

        Device = self.Meta.model
        # if request authenticated, unique together with registration_id and
        # user
        user = self.context["request"].user
        registration_id = attrs.get("registration_id")

        if request_method == "update":
            if registration_id:
                if user is not None and user.is_authenticated:
                    devices = Device.objects.filter(
                        registration_id=registration_id
                    ).exclude(id=primary_key)
                    if attrs.get("active", False):
                        devices.filter(~Q(user=user)).update(active=False)
                    devices = devices.filter(user=user)
                else:
                    devices = Device.objects.filter(
                        registration_id=registration_id
                    ).exclude(id=primary_key)
        elif request_method == "create":
            if user is not None and user.is_authenticated:
                devices = Device.objects.filter(
                    registration_id=registration_id)
                devices.filter(~Q(user=user)).update(active=False)
                devices = devices.filter(user=user, active=True)
            else:
                devices = Device.objects.filter(
                    registration_id=registration_id)

        if devices:
            raise ValidationError(
                {"registration_id": "This field must be unique."})
        return attrs


class TopicSerializer(ModelSerializer):
    subscribed = serializers.BooleanField(read_only=True, required=False)

    class Meta:
        model = Topic
        fields = ('id', 'name', 'description', 'subscribed')
