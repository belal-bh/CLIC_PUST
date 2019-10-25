from django.urls import path
from .coreviews import (
    about_pust,
    about_clic,
    about_faculty,
    about_department,
    about_institute,
    about_administration,
    about_dormitory,
    about_contact,

    about_underconstruction,
)

app_name = 'about'
urlpatterns = [
    path('pust/', about_pust, name='pust'),
    path('clic/', about_clic, name='clic'),
    path('faculty/', about_faculty, name='faculty'),
    path('department/', about_department, name='department'),
    path('institute/', about_institute, name='institute'),
    path('administration/', about_administration, name='administration'),
    path('dormitory/', about_dormitory, name='dormitory'),
    path('contact/', about_contact, name='contact'),


    path('underconstruction/', about_contact, name='underconstruction'),
]
