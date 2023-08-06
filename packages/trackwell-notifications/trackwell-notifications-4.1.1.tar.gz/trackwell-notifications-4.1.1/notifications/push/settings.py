# The origianl code here comes from the fcm-django model and is subject
# to an MIT license. We may have modified the code from the original source to fit our needs.
# For original source see: https://github.com/xtrinch/fcm-django

from django.conf import settings
from django.utils.translation import gettext_lazy as _

SETTINGS = getattr(settings, "PUSH_NOTIFICATION_SETTINGS", {})

# FCM
SETTINGS.setdefault("DEFAULT_FIREBASE_APP", None)
SETTINGS.setdefault("APP_VERBOSE_NAME", _("FCM Django"))
SETTINGS.setdefault("ONE_DEVICE_PER_USER", False)
SETTINGS.setdefault("DELETE_INACTIVE_DEVICES", False)
SETTINGS.setdefault("UPDATE_ON_DUPLICATE_REG_ID", False)

# User model
SETTINGS.setdefault("USER_MODEL", settings.AUTH_USER_MODEL)

SETTINGS.setdefault(
    "ERRORS",
    {
        "invalid_registration": "InvalidRegistration",
        "missing_registration": "MissingRegistration",
        "not_registered": "NotRegistered",
        "invalid_package_name": "InvalidPackageName",
    },
)
