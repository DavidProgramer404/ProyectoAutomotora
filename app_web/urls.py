from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_app'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.CustomLoginView, name='login'),
    path('home/', views.home, name='home'),  # Asegúrate de tener una vista 'home'
]