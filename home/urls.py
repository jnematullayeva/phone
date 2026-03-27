from django.urls import path
from .views import home_views

# home/urls.py
urlpatterns = [
    path('', home_views, name='home'),
]
