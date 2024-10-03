from django.contrib import admin
from . import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "message", "created_at", "updated_at")
    

@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("language",)
    

@admin.register(models.Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ("theme",)
