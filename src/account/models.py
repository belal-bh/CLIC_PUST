# accounts.models.py
import time
from django.urls import reverse
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# from notifications.signals import notify
from account.helpers import UploadTo, DefaultPeriod

CONTACT_MOBILE_REGEX = '^(?:\+?88|0088)?01[15-9]\d{8}$'
CONTACT_PHONE_REGEX = '^(?:\+?88|0088)?0\d{10}$'
LIBRARY_ID_REGEX = '^[a-zA-Z0-9.+-]+$'


class UserManager(BaseUserManager):
    def create_user(self, library_id, email, contact_mobile, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            library_id=library_id,
            email=self.normalize_email(email),
            contact_mobile=contact_mobile
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, library_id, email, contact_mobile, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            library_id,
            email,
            password=password,
            contact_mobile=contact_mobile
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, library_id, email, contact_mobile, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            library_id,
            email,
            password=password,
            contact_mobile=contact_mobile
        )
        user.admin = True
        user.staff = True
        user.save(using=self._db)
        return user

    def active(self, *args, **kwargs):
        return super(UserManager, self).filter(active=True)


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    name = models.CharField(max_length=40, null=True, blank=True)

    father_name = models.CharField(max_length=40, null=True, blank=True)
    mother_name = models.CharField(max_length=40, null=True, blank=True)

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
    mailing_address = models.CharField(max_length=255, null=True, blank=True)
    permanent_address = models.CharField(max_length=255, null=True, blank=True)
    contact_mobile = models.CharField(
        max_length=32,
        validators=[
            RegexValidator(
                regex=CONTACT_MOBILE_REGEX,
                message='Mobile number must be numeric',
                code='invalid_contact_mobile'
            )],
    )
    contact_phone = models.CharField(
        max_length=32,
        validators=[
            RegexValidator(
                regex=CONTACT_PHONE_REGEX,
                message='Phone number must be numeric',
                code='invalid_contact_phone'
            )],
        null=True,
        blank=True
    )
    image = models.ImageField(
        default='account/user/image/default.png',
        upload_to=UploadTo('image', plus_id=True),
        null=True,
        blank=True,
        width_field="width_field",
        height_field="height_field"
    )
    height_field = models.IntegerField(default=0, null=True)
    width_field = models.IntegerField(default=0, null=True)

    STUDENT = 'sn'
    TEACHER = 'tc'
    OFFICER = 'of'
    STAFF = 'sf'
    OTHERMEMBER = 'om'
    LIBRARIAN = 'lb'
    ACCOUNT_TYPE_CHOICES = (
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
        (OFFICER, 'Officer'),
        (STAFF, 'Staff'),
        (OTHERMEMBER, 'Others'),
        (LIBRARIAN, 'Librarian'),
    )
    account_type = models.CharField(
        max_length=2,
        choices=ACCOUNT_TYPE_CHOICES,
        default=STUDENT
    )
    registration_copy = models.FileField(
        upload_to=UploadTo('registration', plus_id=True),
        null=True,
        blank=True
    )
    library_id = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=LIBRARY_ID_REGEX,
                message='Library ID must be alphanumeric or contain numbers',
                code='invalid_library_id'
            )],
        unique=True
    )
    no_borrowed_books = models.PositiveSmallIntegerField(
        default=0,
        null=True,
        blank=True
    )
    no_borrowed_resources = models.PositiveSmallIntegerField(
        default=0,
        null=True,
        blank=True
    )
    validity = models.DateTimeField(
        auto_now=False, auto_now_add=False, default=DefaultPeriod(years=1, hour=10))  # need customization

    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser
    # notice the absence of a "Password field", that's built in.

    USERNAME_FIELD = 'email'
    # Email & Password are required by default.
    REQUIRED_FIELDS = ['library_id', 'contact_mobile']

    objects = UserManager()

    def __str__(self):
        return self.email

    # def get_absolute_url(self):
    #     return reverse("accounts:profile")

    # def get_user_url(self):
    #     return reverse("accounts:user", kwargs={'id': self.id})

    # def get_profile_update_url(self):
    #     return reverse("accounts:profile_update")

    def get_full_name(self):
        # The user is identified by their email address
        if self.name:
            return self.name
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def has_perm(self, perm, obj=None):
        # "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        # "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        # "Is the user a member of staff?"
        return self.staff

    @property
    def is_superuser(self):
        # "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        # "Is the user active?"
        return self.active


@receiver(pre_save, sender=User)
def pre_save_user_receiver(sender, instance, *args, **kwargs):
    if instance:
        print("pre_save_user_receiver -> OK")
    else:
        print("pre_save_user_receiver -> instance was None!")


@receiver(post_save, sender=User)
def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if instance:
        print("post_save_user_receiver done!")
    else:
        print("post_save_user_receiver instance is None!")
