from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse

from account.helpers import UploadTo
from academic.models import Department

class AuthorManager(models.Manager):
    def available(self, *args, **kwargs):
        return super(AuthorManager, self).all()

class BookManager(models.Manager):
    def available(self, *args, **kwargs):
        status_available = 'available'
        return super(BookManager, self).filter(status=status_available)

class ResourceManager(models.Manager):
    def available(self, *args, **kwargs):
        status_available = 'available'
        return super(ResourceManager, self).filter(status=status_available)



class Author(models.Model):
    name = models.CharField(max_length=100)
    nicname = models.CharField(max_length=30)

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
    weblinks = ArrayField(models.CharField(max_length=120),null=True, blank=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        null=True,
        blank=True,
    )
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    objects = AuthorManager()

    def __str__(self):
        if self.name:
            return self.name
        return self.nicname

    class Meta:
        ordering = ["name", "nicname"]


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
    barcode = models.CharField(max_length=255, null=True, blank=True)
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
    departments = models.ManyToManyField(Department)
    tags = ArrayField(models.CharField(max_length=50), null=True, blank=True)
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    work_done = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=15, default="available", null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = BookManager()

    def __str__(self):
        if self.title:
            return self.title
        return self.call_number

    class Meta:
        ordering = ["title", "call_number"]

    def get_absolute_url(self):
        return reverse("resource:bookdetail", kwargs={"id": self.id})


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
    barcode = models.CharField(max_length=255, null=True, blank=True)
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
    departments = models.ManyToManyField(Department)
    tags = ArrayField(models.CharField(max_length=50), blank=True)
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    work_done = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=15, default="available", null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = ResourceManager()

    def __str__(self):
        if self.title:
            return self.title
        return self.call_number

    class Meta:
        ordering = ["title", "call_number"]

    def get_absolute_url(self):
        return reverse("resource:resdetail", kwargs={"id": self.id})
