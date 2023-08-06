from django.conf import settings
from django.db import connection


def get_tenant_identifier() -> str:
    """Get name used to identify notification by tenant.
    Note that this is very specific to Timon needs.

    Returns:
        str: Tenant identifier
    """
    try:
        return connection.get_threadlocal().get_db_name()
    except Exception:
        return getattr(settings, 'WEB_NAME', '')


def get_default_language() -> str:
    """Gets default language to fallback on when sending notifications
    Tries a Tímon specific import, but falls back on LANGUAGE_CODE in settings if that fails

    Returns:
        str: Language code for default language
    """
    default = getattr(settings, 'LANGUAGE_CODE', 'is')
    try:
        # Timon specific import that is allowed to fail
        from customers.models import Customer
        return getattr(Customer.current(), 'language', default)
    except ImportError:
        return default
