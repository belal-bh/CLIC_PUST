from django.urls import path
from .views import (
    dev_view,
)

app_name = 'dev'
urlpatterns = [
    path('secure/', dev_view, name='secure'),
]

