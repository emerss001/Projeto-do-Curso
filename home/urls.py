from unicodedata import name    
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.home, name='home')
]