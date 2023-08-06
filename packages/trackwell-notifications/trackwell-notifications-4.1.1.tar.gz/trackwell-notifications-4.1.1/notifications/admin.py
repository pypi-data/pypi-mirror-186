# -*- coding: utf-8 -*-
from datetime import datetime

from django.conf import settings
from django.contrib import admin
from django.forms import ModelForm, ValidationError
from django.utils.translation import gettext_lazy as _

from notifications.models import UserDevice

from .models import (
    Notification,
    UserNotification
)


@admin.register(UserNotification)
class UserNotificationAdmin(admin.ModelAdmin):
    actions = ['really_delete_selected', 'send_push_notifications']

    list_display = (
        'user',
        'notification'
    )

    search_fields = (
        'user__username',
        'notification__name'
    )
    ordering = ('user__username', 'notification__name')

    def get_actions(self, request):
        actions = super(UserNotificationAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    @admin.action(description="Delete selected entries")
    def really_delete_selected(self, request, queryset):
        for obj in queryset:
            obj.delete()

        # The queryset cache has the count after the loop above, no
        # need for extra call or storing count in variable.
        if queryset.count() == 1:
            message_bit = "1 UserNotification entry was"
        else:
            message_bit = "%s usernotification entries were" % queryset.count()
        self.message_user(request, "%s successfully deleted." % message_bit)

    @admin.action(description=_('Send push notifications'))
    def send_push_notifications(self, request, queryset):
        for un in queryset.filter(notification__notification_type=Notification.TypeChoices.PUSH):
            un.send_push_notification()


class NotificationForm(ModelForm):
    class Meta:
        model = Notification
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        is_push = cleaned_data.get('notification_type') == Notification.TypeChoices.PUSH
        if is_push and not cleaned_data.get('topic'):
            raise ValidationError({'topic': _('Push notifications must have a topic')})
        return cleaned_data


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    actions = ['send_push_notifications']
    readonly_fields = ('management', )
    fields = (
        'name_en',
        'name_is',
        'message_en',
        'message_is',
        'description_en',
        'description_is',
        'notification_type',
        'topic',
        'active_from',
        'expires',
        'needs_approval',
        'snooze_time',
        'groups',
        'look',
        'image',
        'management',
    )
    list_display = (
        'name',
        'notification_type',
        'topic',
        'expires',
        'look',
        'needs_approval',
    )
    list_filter = (
        'notification_type',
        'topic',
        'look',
        'needs_approval',
    )
    ordering = ('-id', )
    form = NotificationForm

    @admin.display(description='Management')
    def management(self, instance):
        EXCLUDED_FIELDS = [
            'groups',
            'id',
            'recipients',
            'attachment',
            'active_from',
            'snooze_lock',
            'recipients',
        ]
        params = ''
        for field in instance.__class__._meta.get_fields():
            if field.name in EXCLUDED_FIELDS:
                continue
            attr = getattr(instance, field.name, None)
            if attr is None or attr == '':
                continue
            if isinstance(attr, datetime):
                attr = attr.isoformat()
            if field.name == 'message':
                attr = ''.join(attr.split('\n'))
                attr = ''.join(attr.split('\r'))
            params += ' --{}=\'{}\''.format(field.name, attr)
        groups = ','.join(map(str, instance.groups.values_list('id', flat=True)))
        if groups:
            params += ' --groups={}'.format(groups)

        return "python manage.py import_notification{}".format(params)

    @admin.action(description=_('Send push notifications'))
    def send_push_notifications(self, request, queryset):
        for notification in queryset.filter(notification_type=Notification.TypeChoices.PUSH):
            notification.send_push_notifications()

    def save_model(self, request, obj, form, change):
        super(NotificationAdmin, self).save_model(request, obj, form, change)
        for group in form.cleaned_data['groups']:
            for user in group.user_set.all():
                UserNotification.objects.get_or_create(notification=obj, user=user)


@admin.register(UserDevice)
class UserDeviceAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'device_id',
        'type',
        'active',
        'name',
        'date_created',
        'registration_id',
    )
    readonly_fields = '__all__'
