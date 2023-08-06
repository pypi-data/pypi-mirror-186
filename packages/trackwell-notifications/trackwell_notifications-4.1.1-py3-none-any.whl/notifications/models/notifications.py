# -*- coding: utf-8 -*-
import datetime
import reversion
from typing import Any, Optional

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.cache import cache
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from firebase_admin.messaging import Message, Notification as FirebaseNotification
from tinymce.models import HTMLField

from notifications.utils import get_default_language


User = get_user_model()


class NotificationError(Exception):
    ...


class NotificationAbstractModel(models.Model):
    class NotificationChoices(models.TextChoices):
        SIGN_COMPANY = 'SIGN_COMPANY'
        SIMPLE_OK = 'SIMPLE_OK'
        RELEASE_NOTES = 'RELEASE_NOTES'

    class TypeChoices(models.IntegerChoices):
        WEB = 0, _('Web notification')
        PUSH = 1, _('Push notification')
        EMAIL = 2, _('Email notification (not implemented)')

    name = models.CharField(
        max_length=250,
        help_text="Used to reference notification, shown in title for some looks",
    )
    description = models.CharField(
        _('Description'),
        max_length=500,
        blank=True,
        default='',
        help_text=_('Short version of the message, mainly for push notifications'),
    )
    message = HTMLField(
        help_text="Full message as shown to user",
    )
    expires = models.DateTimeField(
        default=None,
        null=True,
        blank=True,
        help_text="Notification will not be shown after this time.",
    )
    attachment = models.FileField(
        default=None,
        blank=True,
        null=True,
    )
    active_from = models.DateTimeField(
        default=None,
        null=True,
        blank=True,
    )
    needs_approval = models.BooleanField(
        default=False,
        help_text="Set this field if approval is necessary, see snooze time.",
    )
    snooze_lock = models.IntegerField(
        default=None,
        null=True,
        blank=True,
    )
    snooze_time = models.IntegerField(
        default=None,
        null=True,
        blank=True,
        help_text="If user dismisses message (when relevant), message is shown again after this many days.",
    )  # Days
    # SIGN_COMPANY set as default because it's the only one current existing, safe to remove
    look = models.CharField(
        max_length=50,
        choices=NotificationChoices.choices,
        default=NotificationChoices.SIMPLE_OK,
        help_text="This controls the appearance of the notification.",
    )
    notification_type = models.IntegerField(
        _('Notification type'),
        choices=TypeChoices.choices,
        default=TypeChoices.WEB
    )
    image = models.ImageField(
        upload_to='notification_imgs',
        null=True,
        blank=True,
        help_text="Image to accompany notification (optional)",
    )
    display_only_if_url_path_matches_regex = models.CharField(
        max_length=64,
        default='.*',
        null=False,
        blank=False,
        help_text='Only display this notification if the provided regex matches the url-path',
    )

    class Meta:
        verbose_name = _('Notification')
        verbose_name_plural = _('Notifications')
        abstract = True

    def __str__(self) -> str:
        return self.name

    @property
    def is_web(self) -> bool:
        return self.notification_type == self.TypeChoices.WEB

    @property
    def is_push(self) -> bool:
        return self.notification_type == self.TypeChoices.PUSH


@reversion.register()
class Notification(NotificationAbstractModel):
    external_id = models.IntegerField(
        null=True,
        help_text="Used to reference externally created notifications",
    )
    recipients = models.ManyToManyField(
        User,
        through='UserNotification',
        default=None,
        blank=True,
    )
    groups = models.ManyToManyField(
        Group,
        default=None,
        blank=True,
    )
    topic = models.ForeignKey(
        'Topic',
        verbose_name=_('Push notification topic'),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    @classmethod
    def notification_key(cls, user: User) -> str:
        """Get notification key as it is referred to in cache

        Args:
            user (User): User instance

        Returns:
            str: Cache key
        """
        return f'notifications_unseen:{user.id}'

    @classmethod
    def unseen(cls, user: User) -> dict:
        """Get unseen notifications for user

        Args:
            user (User): User instance

        Returns:
            dict: Unseen notifications
        """
        notifications = cache.get(cls.notification_key(user), default={})
        for user_notif_id in notifications:
            # To make sure cache is up to date for existing notifications
            # before cookies are populated.
            upd_notif = cache.get(cls.notification_key(user), default={})
            if (user_notif := UserNotification.objects.filter(
                id=user_notif_id,
                notification__notification_type=NotificationAbstractModel.TypeChoices.WEB
            ).first()) is not None:
                user_notif.update_unseen_cache(unseen=upd_notif)

        updated_notifications = cache.get(cls.notification_key(user), default={})
        return updated_notifications

    def create_usernotifications_for_groups(self, database_name: Optional[str] = None) -> None:
        """Create user notifications for groups

        Args:
            database_name (Optional[str], optional): Database name to use. Defaults to None.
        """
        for group in self.groups.all():
            for user in group.user_set.all():
                if database_name is not None:
                    UserNotification.objects.using(database_name).get_or_create(notification=self, user=user)
                else:
                    UserNotification.objects.get_or_create(notification=self, user=user)

    def send_push_notifications(self) -> None:
        """Send push notifications to all
        """
        if not self.is_push or self.topic is None:
            return
        extra_filter = Q()
        user_ids = set(self.groups.values_list('user__id', flat=True))
        user_ids.update(set(self.recipients.values_list('id', flat=True)))
        if None in user_ids:
            user_ids.remove(None)
        if user_ids:
            extra_filter = Q(user__in=user_ids)
        self.topic.send_notification(self, extra_filter)

    def get_push_notification_messages(self) -> dict:
        """Generate push notification in all languages

        Returns:
            dict: _description_
        """
        return {
            'en': Message(notification=FirebaseNotification(title=self.name_en, body=self.description_en)),
            'is': Message(notification=FirebaseNotification(title=self.name_is, body=self.description_is)),
            'default': Message(notification=FirebaseNotification(title=self.name, body=self.description))
        }

    def save(self, *args, **kwargs):
        """Override save so it creates user notifications after saving"""
        super(Notification, self).save(*args, **kwargs)
        using = kwargs.get('using', None)
        if not self.is_push and self.groups.exists():
            self.create_usernotifications_for_groups(database_name=using)



@reversion.register()
class UserNotification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    seen = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    next_display = models.DateTimeField(default=None, null=True, blank=True)
    answer = models.BooleanField(default=None, null=True, blank=True)
    answer_string = models.CharField(max_length=255, default=None, blank=True, null=True)

    class Meta:
        verbose_name = _('User notification')
        verbose_name_plural = _('User notifications')

    def __str__(self) -> str:
        return "{} - {} - seen:{} - answer:{} - answer_string:{}".format(
            self.notification.name,
            self.user.username,
            self.seen,
            self.answer,
            self.answer_string
        )

    def update_unseen_cache(self, unseen: Optional[dict] = None) -> Any:
        """Updates unseen notifications in cache

        Args:
            unseen (Optional[dict], optional): Unseen items. Defaults to None.

        Returns:
            Any: Return value from cache methods
        """
        if unseen is None:
            unseen = Notification.unseen(self.user)

        if (self.seen and self.answer) or (
            self.notification.expires is not None and self.notification.expires < datetime.datetime.now()
        ):
            if self.id in unseen:
                del unseen[self.id]
        elif self.next_display:
            unseen[self.id] = self.next_display
        else:
            # 10 Minute in the past to make up for discrepancy between client time and server time
            unseen[self.id] = datetime.datetime.now() - datetime.timedelta(minutes=10)
        if len(unseen) == 0:
            return cache.delete(Notification.notification_key(self.user))
        return cache.set(Notification.notification_key(self.user), unseen, timeout=None)

    def send_push_notification(self) -> None:
        """Send push notification for this notification"""
        if not self.notification.is_push:
            return
        default_language = get_default_language()
        profile = getattr(self.user, 'profile', None)
        prefs = getattr(profile, 'prefs', {})
        language = prefs.get('language', default_language)
        messages = self.notification.get_push_notification_messages()
        msg = messages.get(language, messages.get(default_language))
        if msg is not None:
            Device.objects.filter(user=self.user).send_message(msg)

    def save(self, *args, **kwargs) -> None:
        """Override save so it updates cache and does some snoozing"""
        if self.answer is not None:
            self.seen = True
        if self.seen and not self.answer:
            snooze_time = self.notification.snooze_time or 1
            self.next_display = datetime.datetime.now() + datetime.timedelta(days=snooze_time)
        super(UserNotification, self).save(*args, **kwargs)
        if self.notification.is_web:
            self.update_unseen_cache()

    def delete(self, *args, **kwargs) -> None:
        """Override delete so it clears notification from cache as well"""
        super(UserNotification, self).delete(*args, **kwargs)
        cache.delete(Notification.notification_key(self.user))

    @staticmethod
    def update_for_user(user: User) -> None:
        """Update notifications for user

        Args:
            user (User): User instance
        """
        uns = user.usernotification_set.exclude(answer=True).filter(
            Q(notification__expires=None) | Q(notification__expires__gt=datetime.datetime.now())
        ).filter(notification__notification_type=NotificationAbstractModel.TypeChoices.WEB)

        # Here to ensure cache is up to date
        for un in uns:
            un.update_unseen_cache()
