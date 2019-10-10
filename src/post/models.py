from django.db import models
from django.conf import settings

from account.helpers import UploadTo


class Post(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
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
    draft = models.BooleanField(default=False)
    published = models.DateField(auto_now=False, auto_now_add=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
