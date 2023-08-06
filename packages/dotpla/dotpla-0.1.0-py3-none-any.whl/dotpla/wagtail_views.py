"""Views for Wagtail projects."""

import logging

from django.contrib import messages
from wagtail.contrib.modeladmin.views import CreateView

logger = logging.getLogger(__name__)


class CreateOTPLAView(CreateView):
    """View to create OTP Link Auth credentials in the Wagtail Admin."""

    def form_valid(self, form):
        """Override the Wagtail provided method."""

        result = super().form_valid(form)
        otp = self.instance

        # This should always be empty on creation, but an if won't hurt regardless
        if not otp.otp_hash:
            pw = otp.generate_random_password()
            otp.set_otp_hash(pw)
            # Display the generated password upon creation.
            messages.add_message(
                self.request,
                messages.SUCCESS,
                f"Your One Time Password is '{pw}'. Copy it now; it will not be displayed again.",
                ["dotpla-pw-success"],
            )

        return result
