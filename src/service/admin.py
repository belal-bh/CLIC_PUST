from django.contrib import admin

from .models import (
    Request,
    Report,
    Notice,
)

admin.site.register(Request)
admin.site.register(Report)
admin.site.register(Notice)
