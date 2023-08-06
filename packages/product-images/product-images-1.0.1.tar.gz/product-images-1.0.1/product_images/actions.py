
from django.utils.translation import gettext_lazy as _

from product_images.utils import refresh_logo


def refresh_logos(modeladmin, request, queryset):
    for instance in queryset:
        refresh_logo(instance)

refresh_logos.short_description = _('Refresh logos')
