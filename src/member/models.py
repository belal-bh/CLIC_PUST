from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator

from academic.models import Faculty, Department, Program

CONTACT_MOBILE_REGEX = '^(?:\+?88|0088)?01[15-9]\d{8}$'
CONTACT_PHONE_REGEX = '^(?:\+?88|0088)?0\d{10}$'


class Student(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    student_id = models.CharField(
        max_length=20,
        unique=True
    )
    student_roll = models.CharField(
        max_length=20,
        unique=True
    )

    local_guardian_name = models.CharField(
        max_length=40, null=True, blank=True)
    guardian_contact_mobile = models.CharField(
        max_length=32,
        validators=[
            RegexValidator(
                regex=CONTACT_MOBILE_REGEX,
                message='Mobile number must be numeric',
                code='invalid_contact_mobile'
            )],
    )
    guardian_contact_phone = models.CharField(
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
    faculty = models.ForeignKey(
        Faculty, on_delete=models.SET_NULL, blank=True,
        null=True,
    )
    program = models.ForeignKey(
        Program, on_delete=models.SET_NULL, blank=True,
        null=True,
    )
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, blank=True,
        null=True,
    )
    session = models.CharField(max_length=15)
    year = models.CharField(max_length=15)
    semester = models.CharField(max_length=15)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)


class Teacher(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    teacher_id = models.CharField(
        max_length=20,
        unique=True
    )
    designation = models.CharField(max_length=40)
    faculty = models.ForeignKey(
        Faculty, on_delete=models.SET_NULL, blank=True,
        null=True,
    )
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, blank=True,
        null=True,
    )
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)


class Officer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    officer_id = models.CharField(
        max_length=20,
        unique=True
    )
    designation = models.CharField(max_length=40)
    department = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)


class Staff(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='staff_user',
        on_delete=models.CASCADE,
    )
    staff_id = models.CharField(
        max_length=20,
        unique=True
    )
    designation = models.CharField(max_length=40)
    department = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)


class Othermember(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    member_id = models.CharField(
        max_length=20,
        unique=True
    )
    designation = models.CharField(max_length=40)
    department = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)


class Librarian(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    designation = models.CharField(max_length=40)

    # need to discuss about various member_type
    STAFF = 'staff'
    ADMIN = 'admin'
    MEMBER_TYPE_CHOICES = (
        (STAFF, 'Staff'),
        (ADMIN, 'Admin'),
    )
    member_type = models.CharField(
        max_length=10,
        choices=MEMBER_TYPE_CHOICES,
        default=STAFF
    )
    active = models.BooleanField(default=True)
    validity = models.DateTimeField(
        auto_now=False, auto_now_add=True)  # need customization
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
