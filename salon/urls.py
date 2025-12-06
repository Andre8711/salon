from django.urls import path
from . import views

urlpatterns = [
    path('', views.active_salons, name='home'),  # Главная страница
    path('active_salons/', views.active_salons, name='active_salons'),
    path('salon/<int:salon_id>/', views.salon_detail, name='salon_detail'),
    path('first_active_salon/', views.first_active_salon, name='first_active_salon'),
    path('top_masters/', views.top_masters, name='top_masters'),
    path('experienced_hairdressers/', views.experienced_hairdressers, name='experienced_hairdressers'),
    path('new_masters_2023/', views.new_masters_2023, name='new_masters_2023'),
    path('hair_services/', views.hair_services, name='hair_services'),
 
    path('budget_services/', views.budget_services, name='budget_services'),
    path('good_masters/', views.good_masters, name='good_masters'),
]