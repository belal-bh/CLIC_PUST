from django.db import models
from django.conf import settings
from resource.models import (
    Book,
    Resource
)

class BookCartManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(BookCartManager, self) #.filter(draft=False).filter(publish__lte=timezone.now())

class ResourceCartManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(ResourceCartManager, self) #.filter(draft=False).filter(publish__lte=timezone.now())


class BookCart(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False)
    comment = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = BookCartManager()

    def __str__(self):
        return self.book.title

class ResourceCart(models.Model):
    resource = models.ForeignKey(
        Resource, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False)
    comment = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = ResourceCartManager()
