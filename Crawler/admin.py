from django.contrib import admin
from .models import Platform, Channel, Config


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ['name', 'active']
    list_filter = ['active',]
    search_fields = ['name']


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ['name', 'platform', 'active']
    list_filter = ['platform', 'active',]
    search_fields = ['name', 'platform', ]


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    pass
