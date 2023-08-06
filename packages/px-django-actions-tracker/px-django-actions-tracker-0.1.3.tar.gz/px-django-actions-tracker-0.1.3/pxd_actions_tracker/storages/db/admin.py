from django.contrib import admin
from django.utils.translation import pgettext_lazy
from django.db import models
from prettyjson import PrettyJSONWidget
from django.utils import timezone, formats

from .models import Log


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = 'id', 'domain', 'message', 'tracking', 'created_at_extended',
    list_display_links = 'id', 'message',
    list_filter = (
        # 'domain',
        'created_at',
    )
    search_fields = 'id', 'domain', 'tracking', 'message', 'detail',
    readonly_fields = 'id', 'domain', 'tracking', 'message', 'created_at_extended',
    date_hierarchy = 'created_at'

    fieldsets = (
        (
            None,
            {
                'fields': (
                    ('domain', 'message'),
                    'detail',
                    'tracking',
                    'created_at_extended',
                )
            }
        ),
    )

    formfield_overrides = {models.JSONField: {'widget': PrettyJSONWidget}}

    def created_at_extended(self, obj):
        return '{} {}'.format(
            formats.localize(timezone.template_localtime(obj.created_at)),
            obj.created_at.strftime('%S.%f'),
        )

    created_at_extended.admin_order_field = 'created_at'
    created_at_extended.short_description = pgettext_lazy(
        'pxd-actions-tracker', 'Created at'
    )
