from django.contrib import admin
from .models import FCMSettings, UserFcmToken, UserMobileFcmToken


@admin.register(FCMSettings)
class FCMSettingsAdmin(admin.ModelAdmin):
    list_display = ['version', 'is_active', 'api_key']
    list_display_links = ['version', 'is_active', 'api_key']
    search_fields = ['version', 'is_active', 'api_key']
    readonly_fields = ['last_updated']


@admin.register(UserFcmToken)
class UserFcmTokenAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'fcm_token'
    ]
    readonly_fields = [
        'fcm_token', 'last_updated', 'created_at',
    ]


@admin.register(UserMobileFcmToken)
class UserMobileFcmTokenAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'fcm_token'
    ]
    readonly_fields = [
        'fcm_token', 'last_updated', 'created_at',
    ]
