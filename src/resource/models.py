from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField

from account.helpers import UploadTo
from academic.models import Department


class Author(models.Model):
    name = models.CharField(max_length=40)
    nicname = models.CharField(max_length=20)

    MALE = 'm'
    FEMALE = 'f'
    OTHERS = 'o'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS, 'Others'),
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default=MALE
    )
    nationality = models.CharField(max_length=20, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    weblinks = models.CharField(null=True, blank=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        null=True,
        blank=True,
    )
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ManyToManyField(Author)
    edition = models.CharField(max_length=20, null=True, blank=True)
    pagination = models.PositiveIntegerField(null=True, blank=True)
    # need customization later: uniqe or not
    accession_number = models.CharField(max_length=50, unique=True)
    call_number = models.CharField(max_length=20)  # need customization
    copy_number = models.CharField(max_length=20)  # need customization
    # need customization later: uniqe or not
    isbn = models.CharField(max_length=50)
    publisher = models.CharField(max_length=120, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    language = models.CharField(max_length=20)
    publication_date = models.DateField(null=True, blank=True)
    last_revision_date = models.DateField(null=True, blank=True)
    mrp = models.PositiveIntegerField(null=True, blank=True)
    barcode = models.CharField(null=True, blank=True)
    image = models.ImageField(
        default='resource/book/image/default.png',
        upload_to=UploadTo('image', plus_id=True),
        null=True,
        blank=True,
        width_field="width_field",
        height_field="height_field"
    )
    height_field = models.IntegerField(default=0, null=True)
    width_field = models.IntegerField(default=0, null=True)
    departments = models.ManyToManyField(Department, null=True, blank=True)
    tags = ArrayField(models.CharField(max_length=50), blank=True)
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    work_done = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=15, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


class Resource(models.Model):
    title = models.CharField(max_length=255)

    # Need to add or customize later
    SOFTWARE = 'software'
    HARDWARE = 'hardware'
    MAGAZINE = 'magazine'
    OTHER = 'other'
    RESOURCE_TYPE_CHOICES = (
        (SOFTWARE, 'Software'),
        (HARDWARE, 'Hardware'),
        (MAGAZINE, 'Magazine'),
        (OTHER, 'Other'),
    )
    resource_type = models.CharField(
        max_length=20,
        choices=RESOURCE_TYPE_CHOICES,
        default=OTHER,
    )
    # need customization later: uniqe or not
    accession_number = models.CharField(max_length=50)
    call_number = models.CharField(max_length=20)  # need customization
    copy_number = models.CharField(max_length=20)  # need customization
    description = models.TextField(null=True, blank=True)
    mrp = models.PositiveIntegerField(null=True, blank=True)
    barcode = models.CharField(null=True, blank=True)
    image = models.ImageField(
        default='resource/resource/image/default.png',
        upload_to=UploadTo('image', plus_id=True),
        null=True,
        blank=True,
        width_field="width_field",
        height_field="height_field"
    )
    height_field = models.IntegerField(default=0, null=True)
    width_field = models.IntegerField(default=0, null=True)
    departments = models.ManyToManyField(Department, null=True, blank=True)
    tags = ArrayField(models.CharField(max_length=50), blank=True)
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    work_done = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=15, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
