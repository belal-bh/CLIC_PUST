from django.db import models


class Faculty(models.Model):
    faculty_id = models.CharField(
        max_length=20,
        unique=True,
    )
    name = models.CharField(max_length=120)
    abbreviation = models.CharField(max_length=15)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


class Department(models.Model):
    dept_id = models.CharField(
        max_length=20,
        unique=True,
    )
    name = models.CharField(max_length=120)
    abbreviation = models.CharField(max_length=15)
    faculty = models.ForeignKey(
        Faculty, on_delete=models.SET_NULL, blank=True,
        null=True,
    )
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


class Program(models.Model):
    program_id = models.CharField(
        max_length=20,
        unique=True,
    )
    name = models.CharField(max_length=120)
    abbreviation = models.CharField(max_length=15)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
