from django.contrib import admin

from .models import (
    Faculty,
    Department,
    Program,
)

admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Program)
