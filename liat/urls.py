"""liat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# urls to main project
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static  import static
from django.views.static import serve
from django.urls import re_path as url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('theblog/', include('theblog.urls')),
    path('photos/', include('photos.urls')),
    path('broker/', include('broker.urls')),
    path('members/', include('members.urls')),
    path('accounts/', include('allauth.urls')),
    path('apply/', include('apply.urls')),
    path('', include("django.contrib.auth.urls")),
    #social app auth
    path('social/', include('social_django.urls', namespace='social')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 


] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)