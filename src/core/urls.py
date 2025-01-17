"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import include
from django.conf.urls.static import static

import notifications.urls

from account.views import (
    login_view,
    register_view,
    logout_view,
    index_page,
)

urlpatterns = [
    path('', index_page, name='index'),
    path('admin/', admin.site.urls),
    path('lib/', include("core.lib.urls", namespace='lib')),

    path('dev/', include('core.dev.urls', namespace='dev')),

    path('about/', include("core.coreurls", namespace='about')),

    path('account/', include("account.urls", namespace='account')),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('resource/', include("resource.urls", namespace='resource')),

    path('blog/', include("post.urls", namespace='blog')),

    path('service/', include("service.urls", namespace='service')),



    path('inbox/notifications/',
         include(notifications.urls, namespace='notifications')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
