from django.contrib import admin

from .models import (
    Student,
    Teacher,
    Officer,
    Staff,
    Othermember,
    Librarian
)

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Officer)
admin.site.register(Staff)
admin.site.register(Othermember)
admin.site.register(Librarian)
