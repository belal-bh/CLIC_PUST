from django.contrib import admin

from .models import (
    Author,
    Book,
    Resource,
)

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Resource)
