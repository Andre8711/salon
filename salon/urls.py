from django.urls import path
from . import views

urlpatterns = [
    path('', views.active_salons, name='home'),  # Главная страница
    path('active_salons/', views.active_salons, name='active_salons'),
    # другие маршруты
]