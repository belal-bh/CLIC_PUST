from django.urls import path
from .views import (
    book_list,
    book_detail,
    resource_list,
    resource_detail,
    resource_doclist,
    resource_newspaperlist,
)

app_name = 'resource'
urlpatterns = [
    path('book/', book_list, name='booklist'),
    path('book/<int:id>/', book_detail, name='bookdetail'),
    path('res/', resource_list, name='reslist'),
    path('res/<int:id>/', resource_detail, name='resdetail'),

    path('doc/', resource_doclist, name='doclist'),
    path('newspaper/', resource_newspaperlist, name='newspaperlist'),
]
