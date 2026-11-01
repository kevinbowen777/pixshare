from typing import ClassVar

from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display: ClassVar[list[str]] = ["user", "date_of_birth", "photo"]
    raw_id_fields: ClassVar[list[str]] = ["user"]
