# links/admin.py

from django.contrib import admin

from .models import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    """
    Customizes the display and functionality of the Link model in the Django Admin.
    """

    list_display = ("link_text", "url", "category", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("link_text", "url", "description", "category")
    readonly_fields = ("created_at", "updated_at")  # These fields are automatically set

    fieldsets = (
        (None, {"fields": ("link_text", "url", "description", "category")}),
        (
            "Timestamps",
            {
                "fields": ("created_at", "updated_at"),
                "classes": ("collapse",),  # Makes this section collapsible
            },
        ),
    )
