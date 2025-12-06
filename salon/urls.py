from django.urls import path
from . import views

urlpatterns = [
    path('', views.active_salons, name='home'),  # Главная страница
    path('active_salons/', views.active_salons, name='active_salons'),
    path('salon/<int:salon_id>/', views.salon_detail, name='salon_detail'),
    path('first_active_salon/', views.first_active_salon, name='first_active_salon'),
]