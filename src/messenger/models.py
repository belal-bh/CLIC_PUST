# messenger.models.py
from django.db import models
from django.conf import settings

from account.helpers import UploadTo


class Message(models.Model):
    content = models.TextField()
    image = models.ImageField(
        upload_to=UploadTo('image', plus_id=True),
        null=True,
        blank=True,
        width_field="width_field",
        height_field="height_field"
    )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    attachments = models.FileField(
        upload_to=UploadTo('attachments', plus_id=True),
        null=True,
        blank=True
    )
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
        related_name='messenger_user_sender')
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
        related_name='messenger_user_receiver')
    parent = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
