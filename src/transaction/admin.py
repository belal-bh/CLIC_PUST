from django.contrib import admin

from .models import (
    TrxBook,
    TrxResource,
)

admin.site.register(TrxBook)
admin.site.register(TrxResource)
