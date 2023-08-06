"""Hooks to integrate this into Wagtail, if available."""

from dotpla.wagtail_views import CreateOTPLAView

from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from epicdev.users.models import OneTimePassLinkAuth


class BaseOTPLAWagtailAdmin(ModelAdmin):
    """Base Model Admin for One Time Pass authentication models for Wagtail."""

    model = OneTimePassLinkAuth
    menu_label = "One Time Password Link Auth"
    menu_icon = "lock"
    menu_order = 503
    add_to_settings_menu = False
    exclude_from_explorer = False
    create_view_class = CreateOTPLAView
    base_url_path = "dotpla"


modeladmin_register(BaseOTPLAWagtailAdmin)
