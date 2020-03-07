from django.contrib import admin

from .models import (
    BookCart,
    ResourceCart,
)

admin.site.register(BookCart)
admin.site.register(ResourceCart)
