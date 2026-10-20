from django.urls import path
from . import views

app_name = 'loja'

urlpatterns = [
    path('teste/', views.ola_mundo, name='ola_mundo'),
]