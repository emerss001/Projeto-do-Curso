from unicodedata import name
from django.urls import URLPattern, path
from . import views


urlpatterns = [
    path('logout/', views.logout, name="logout"),
    path('registrar/', views.cadastrar_usuario, name="cadastrar_usuario"),
]