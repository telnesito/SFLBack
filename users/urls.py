from django.urls import re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    re_path('login', views.login),
    re_path('profile', views.profile),
    re_path('register', views.register),
    
]