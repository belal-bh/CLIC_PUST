from django.urls import path
from .views import (
    post_list,
    post_create,
    post_detail,
    # post_update,
    # post_delete,
)

app_name = 'blog'
urlpatterns = [
    path('post/', post_list, name='postlist'),
    path('post/create/', post_create),
    path('post/<int:id>/', post_detail, name='postdetail'),
    # path('post/<id:int>/edit/', post_update, name='postupdate'),
    # path('post/<id:int>/delete/', post_delete),
]
