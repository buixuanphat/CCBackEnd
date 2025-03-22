from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers, permissions

r = routers.DefaultRouter()
r.register('user', views.UserViewSet)
r.register('file', views.FileViewSet)
urlpatterns = [
    path('', include(r.urls)),
    path('o/', include('oauth2_provider.urls')),
]
