from django.urls import path
from .views import (
    notice_list,
)

app_name = 'service'
urlpatterns = [
    path('notice/', notice_list, name='noticelist'),
]
