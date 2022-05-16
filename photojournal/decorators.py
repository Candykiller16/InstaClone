from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


def is_staff_user_only(function):
    """Limit view to is_staff only."""

    def _inner(request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied
        return function(request, *args, **kwargs)

    return _inner
