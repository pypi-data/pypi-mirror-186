# -*- coding: utf-8 -*-
from urllib.parse import urlparse
import datetime
import operator
import re

from .models import Notification, UserNotification




class NotificationMiddleware(object):
    IGNORED_PATHS = ['jsi18n']

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if self.is_valid_request(request):
            request.notifications = Notification.unseen(request.user)
            response = self.process_response(request, response)
        return response

    def is_valid_request(self, request):
        """Checks if request is valid
        Checks if
            - user is authenticated
            - request path is not in IGNORED_PATHS

        Args:
            request (Request): Request object

        Returns:
            bool: Whether request is valid
        """
        path_split = request.path.split('/')
        is_valid_path = (
            len(path_split) > 1 and path_split[1] not in self.IGNORED_PATHS
        ) or len(path_split) <= 1
        return hasattr(request, 'user') and request.user.is_authenticated and is_valid_path

    def process_response(self, request, response):
        """Process response and add notification values to cookies if appliccable

        Args:
            request (Request): Request instance
            response (Response): Response instanve

        Returns:
            Response: Response with added cookie, if appliccable
        """
        if not self.is_valid_request(request):
            return response

        notifications = Notification.unseen(request.user)
        now = datetime.datetime.now()
        if notifications:
            notifications_keys = notifications.keys()
            notification_value_list = UserNotification.objects.filter(id__in=notifications_keys).values_list(
                'id', 'notification__display_only_if_url_path_matches_regex', 'notification__active_from',
                'notification__expires')
            for notif_id, regex, active_from, expires in notification_value_list:
                if active_from is not None and now < active_from:
                    del notifications[notif_id]
                    continue
                if expires is not None and now > expires:
                    del notifications[notif_id]
                    continue
                matching_path = re.search(regex, request.path) is not None
                if not matching_path and notif_id in notifications:
                    del notifications[notif_id]

        if notifications:
            # Need to ensure cookie string is in reverse order from closest to last
            sorted_items = sorted(notifications.items(), key=operator.itemgetter(1))
            epoch = datetime.datetime.utcfromtimestamp(0)
            max_age = 14 * 24 * 60 * 60
            expires = datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age)

            coookie_string = "-".join(
                '{}:{}'.format(key, (val - epoch).total_seconds() * 1000.0)
                for key, val in sorted_items
            )
            response.set_cookie(
                'notifications', coookie_string, expires=expires
            )
        else:
            response.delete_cookie('notifications')

        return response
