"""Middleware for dotpla."""

import logging

from django.apps import apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

logger = logging.getLogger(__name__)

try:
    auth_model: str = settings.DOTPLA["auth_model"]
    OTPLAModel = apps.get_model(auth_model)
except (AttributeError, KeyError):
    raise ImproperlyConfigured("DOTPLA['auth_model'] is not set.")


class OneTimePassLinkAuthMiddleware:
    """Middleware to authenticate users using URL GET attributes."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check authentication before calling the view and other middleware
        logger.debug(f"Calling {self.__class__.__name__}()")
        otu = request.GET.get("otu")
        otp = request.GET.get("otp")

        if request.user.is_anonymous and otu and otp:
            logger.debug(f"Trying to authenticate with OTP {otu}:{otp}")
            OTPLAModel.authenticate_with_otp(otu, otp, request)

        # Call following middleware and view
        response = self.get_response(request)
        return response
