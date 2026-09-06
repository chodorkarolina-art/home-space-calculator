from django.contrib import admin

from .models import Calculation


@admin.register(Calculation)
class CalculationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "user",
        "adults",
        "children",
        "recommended_area",
        "recommended_rooms",
        "created_at",
    )

    list_filter = (
        "remote_work",
        "hobby",
        "storage_level",
        "created_at",
    )

    search_fields = (
        "name",
        "user__username",
    )

    ordering = (
        "-created_at",
    )