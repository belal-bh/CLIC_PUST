from django.db import models
from django.conf import settings


class Activity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT)
    messege = models.TextField()
    link = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
