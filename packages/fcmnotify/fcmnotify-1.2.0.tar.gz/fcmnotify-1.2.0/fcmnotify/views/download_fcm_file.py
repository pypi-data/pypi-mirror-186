from django.shortcuts import render, get_object_or_404
from fcmnotify.models import FCMSettings
import os


def download_file_preview(request):
    template = 'main.html'
    context = {
        'fcm': get_object_or_404(FCMSettings, is_active=True)
    }
    return render(request, template, context)
