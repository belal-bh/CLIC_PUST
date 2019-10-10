from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from account.helpers import UploadTo


class Comment(models.Model):
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

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    parent = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
