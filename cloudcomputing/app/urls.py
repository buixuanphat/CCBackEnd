from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers, permissions
from django.conf import settings
from django.conf.urls.static import static

r = routers.DefaultRouter()
r.register('user', views.UserViewSet)
r.register('file', views.FileViewSet)
r.register('share', views.FileShareViewSet)
urlpatterns = [
    path('', include(r.urls)),
    path('o/', include('oauth2_provider.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
