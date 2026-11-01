from typing import ClassVar

from django.contrib import admin

from .models import Action


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display: ClassVar[list[str]] = ["user", "verb", "target", "created"]
    list_filter: ClassVar[list[str]] = ["created"]
    search_fields: ClassVar[list[str]] = ["verb"]
