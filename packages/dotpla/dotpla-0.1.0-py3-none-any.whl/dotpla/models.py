"""Models for the dotpla app."""

import logging
import uuid
from typing import Any

from django.contrib.auth import get_user_model, login
from django.contrib.auth.hashers import check_password, make_password
from django.db import models
from django.db.models import F
from django.http import HttpRequest

logger = logging.getLogger(__name__)


class BaseOTPLAModel(models.Model):
    """Base model for One-Time Password Authentication."""

    # A hashed random password
    # Use editable=False to hide this field from the Admin. It will be auto-generated.
    otp_hash = models.CharField(max_length=128, editable=False)
    otp_max_uses = models.PositiveSmallIntegerField(
        help_text="Allow this password to be used up to this many times.",
        default=1,
    )
    otp_use_count = models.PositiveSmallIntegerField(
        help_text="How many times this password has been used. You should not need to edit this.",
        default=0,
    )

    class Meta:
        abstract = True

    @classmethod
    def authenticate_with_otp(cls, otu: str, otp: str, request: HttpRequest) -> None:
        """Get user instance if credentials are valid. This requires a subclass with a user field."""

        # Get the user instance if the username is valid
        user_model = get_user_model()
        try:
            user = user_model.objects.get(username=otu)
        except user_model.DoesNotExist:
            return None

        # Get one time passwords for the user
        link_pws = cls.objects.filter(user=user)

        for pw in link_pws:
            if pw.can_login(user, otp):
                # Warning: potential race condition here that allows logins to be reused.
                pw.use_login()
                login(request, user)

    @staticmethod
    def generate_random_password() -> str:
        """Generates a random password string."""

        # Simply return a completely random UUID, for now
        return str(uuid.uuid4())

    def can_login(self, user: Any, password: str) -> bool:
        """Checks that the credentials are valid, and the user is active."""

        if self.otp_use_count >= self.otp_max_uses:
            return False

        if not user.is_active:
            return False

        return check_password(password, self.otp_hash)

    def set_otp_hash(self, password: str) -> None:
        """Takes a password, hashes it, and stores it encrypted in the otp_hash field."""

        hashed = make_password(password)
        self.otp_hash = hashed
        self.save()

    def use_login(self) -> None:
        """Increase the usage count."""

        self.otp_use_count = F("otp_use_count") + 1
        self.save()
