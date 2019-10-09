# service.models.py
from django.db import models
from django.conf import settings
import uuid

from account.helpers import UploadTo


class Request(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(
        upload_to=UploadTo('image', plus_id=True),
        null=True,
        blank=True,
        width_field="width_field",
        height_field="height_field"
    )
    height_field = models.IntegerField(default=0, null=True)
    width_field = models.IntegerField(default=0, null=True)

    attachments = models.FileField(
        upload_to=UploadTo('attachments', plus_id=True),
        null=True,
        blank=True
    )
    draft = models.BooleanField(default=False)
    published = models.DateTimeField(auto_now=False, auto_now_add=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    ACCEPTED = 'accepted'
    REJECTED = 'rejected'
    PENDING = 'pending'
    OPEN = 'open'
    CLOSED = 'closed'

    STATUS_CHOICES = (
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
        (PENDING, 'Pending'),
        (OPEN, 'Open'),
        (CLOSED, 'Closed'),
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=OPEN
    )
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)


class Report(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(
        upload_to=UploadTo('image', plus_id=True),
        null=True,
        blank=True,
        width_field="width_field",
        height_field="height_field"
    )
    height_field = models.IntegerField(default=0, null=True)
    width_field = models.IntegerField(default=0, null=True)

    attachments = models.FileField(
        upload_to=UploadTo('attachments', plus_id=True),
        null=True,
        blank=True
    )
    draft = models.BooleanField(default=False)
    published = models.DateTimeField(auto_now=False, auto_now_add=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    ACCEPTED = 'accepted'
    REJECTED = 'rejected'
    PENDING = 'pending'
    OPEN = 'open'
    CLOSED = 'closed'

    STATUS_CHOICES = (
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
        (PENDING, 'Pending'),
        (OPEN, 'Open'),
        (CLOSED, 'Closed'),
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=OPEN
    )
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)


class Notice(models.Model):
    notice_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    attachments = models.FileField(
        upload_to=UploadTo('attachments', plus_id=True),
        null=True,
        blank=True
    )
    send_from = models.CharField(max_length=255, null=True, blank=True)
    send_to = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="service_user_send_to")
    draft = models.BooleanField(default=False)
    published = models.DateTimeField(auto_now=False, auto_now_add=False)
    posted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="service_user_posted_by")
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
