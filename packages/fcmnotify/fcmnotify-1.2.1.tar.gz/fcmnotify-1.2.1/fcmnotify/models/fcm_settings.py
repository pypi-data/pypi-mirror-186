# DJANGO IMPORTS
from django.db import models
from django.conf import settings


def media_upload_path(instance, filename):
    """Returns formatted upload to path"""
    ext = filename.split('.')[-1]
    filename_new = "%s_%s_%s.%s" % (f'fcm_file', instance.version, instance.id, ext) # noqa
    path = f'FCM/{instance.version}_file_{instance.pk}/{filename_new}'
    return path


class FCMSettingsManager(models.Manager):
    def active(self):
        return self.get(is_active=True, is_deleted=False)


class FCMSettings(models.Model):
    version = models.CharField(
        verbose_name = ("Version"), max_length=255, unique=True, help_text="FCM-00.1"
    )
    created_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        blank=True, null=True, related_name="%(app_label)s_%(class)s_createdby"
    )
    is_active = models.BooleanField(
       verbose_name = ('Is Active'), default=False
    )
    is_deleted = models.BooleanField(
        verbose_name = ('Is Deleted'), default=False
    )
    created_at = models.DateTimeField(
        verbose_name = ('Created At'), auto_now_add=True, null=True
    )
    last_updated = models.DateTimeField(
        verbose_name = ('Last Updated'), auto_now=True, null=True
    )
    updated_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        blank=True, null=True, related_name="%(app_label)s_%(class)s_updated"
    )
    api_key = models.CharField(
        verbose_name = ("apiKey"), max_length=255, help_text="AIzaSyA33PItbOMuAHiR-x4y7"
    )
    auth_domain = models.CharField(
        verbose_name = ("authDomain"), max_length=255, help_text="f80.firebaseapp.com"
    )
    database_URL = models.CharField(
        verbose_name = ("databaseURL"), max_length=255,
        help_text="https://f80.asia-southeast1.firebasedatabase.app"
    )
    project_id = models.CharField(
        verbose_name = ("projectId"), max_length=255, help_text="sp-90f80"
    )
    storage_bucket = models.CharField(
        verbose_name = ("storageBucket"), max_length=255, help_text="f80.appspot.com"
    )
    messaging_sender_id = models.CharField(
        verbose_name = ("messagingSenderId"), max_length=255, help_text="6219890099"
    )
    app_id = models.CharField(
        verbose_name = ("appId"), max_length=255,
        help_text="1:62168752376:web:d92b54654b50414d"
    )
    measurement_id = models.CharField(
        verbose_name = ("measurementId"), max_length=255, help_text="G-D5D0V879"
    )
    server_key = models.CharField(
        verbose_name = ("serverKey"), max_length=255,
        help_text="key=AAAAkMzqN7g:APA91bFKF9NOhnZJWig.."
    )
    use_public_vapid_key = models.CharField(
        verbose_name = ("usePublicVapidKey"), max_length=255,
        help_text="BAelDrmFfEmTc1t2HHbU-4pABsf2rohKdRk9dtFY...."
    )
    action_domain = models.URLField(
       verbose_name = ("actionDomain"), help_text="Application URL"
    )
    icon_image = models.ImageField(
       verbose_name = ("Icon Image"), upload_to=media_upload_path
    )
    objects = FCMSettingsManager()

    def save(self, *args, **kwargs):
        if self.is_active:
            for fcm in FCMSettings.objects.filter(is_active=True):
                fcm.is_active = False
                fcm.save()
        super(FCMSettings, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.version}'
