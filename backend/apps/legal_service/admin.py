from .models import LegalService
from django.contrib import admin


@admin.register(LegalService)
class LegalServiceAdmin(admin.ModelAdmin):
    """
    Услуга в админке
    """

    list_display = (
        "title",
        "date_updated",
        "date_created",
        "is_published_landing",
    )
    list_filter = ("is_published_landing",)
