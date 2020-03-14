from django.db import models
from django.conf import settings
import uuid

from resource.models import (
    Book, 
    Resource
)

class TrxBookManager(models.Manager):
    # def get_queryset(self, *args, **kwargs):
    #     return super(TrxBookManager, self).get_queryset().filter(status="open")
    def all(self, *args, **kwargs):
        return super(TrxBookManager, self)

class TrxResourceManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super(TrxResourceManager, self).get_queryset() #.filter(status="open")


class TrxBook(models.Model):
    trxid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    issue_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    due_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    return_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    comment = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="trxbook_user_borrower")
    book = models.ForeignKey(
        Book, on_delete=models.PROTECT)
    issued_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="trxbook_user_issued_by", null=True, blank=True)
    status = models.CharField(max_length=15, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    objects = TrxBookManager()

    def __str__(self):
        return self.book.title
    

class TrxResource(models.Model):
    trxid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    issue_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    due_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    return_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    comment = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="trxresource_user_borrower")
    resource = models.ForeignKey(
        Resource, on_delete=models.PROTECT)
    issued_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="trxresource_user_issued_by", null=True, blank=True)
    status = models.CharField(max_length=15, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    objects = TrxResourceManager()

    def __str__(self):
        return self.resource.title