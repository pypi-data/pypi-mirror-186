from django.urls import path
from .views import (
    showFirebaseJS,
    save_user_fcm_token,
    download_file,
    download_file_preview
)
app_name = 'fcmnotify'

urlpatterns = [
    # Firebase...........
    path('save_fcm_token/', save_user_fcm_token, name='save_fcm_token'),
    path(
        'download-fcm-settings/html/download_file/', download_file,
        name='download_fcm_file'
    ),
    path(
        'firebase-messaging-sw.js',
        showFirebaseJS, name="show_firebase_js"
    ),
    path(
        'fcm-settings/', download_file_preview, name="fcm-settings"
    ),
]
