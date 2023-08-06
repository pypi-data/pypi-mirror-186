from django.contrib import admin


class BaseOTPLAModelAdmin(admin.ModelAdmin):
    """Base Model Admin for One Time Pass authentication models."""

    def save_model(self, request, obj, form, change):
        # TODO: generate OTP
        super().save_model(request, obj, form, change)
