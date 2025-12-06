
from django.shortcuts import render, get_object_or_404
from .models import Salon
from .models import Master
from .models import Service

def active_salons(request):
    salons = Salon.objects.filter(is_active=True)
    return render(request, 'salon/active_salons.html', {'salons': salons})
    

def salon_detail(request, salon_id):
    salon = get_object_or_404(Salon, id=salon_id)
    return render(request, 'salon/salon_detail.html', {'salon': salon})

def first_active_salon(request):
    salon = Salon.objects.filter(is_active=True).first()
    return render(request, 'salon/first_active_salon.html', {'salon': salon})

def top_masters(request):
    masters = Master.objects.filter(rating__gt=4.5)
    return render(request, 'salon/top_masters.html', {'masters': masters})

def experienced_hairdressers(request):
    masters = Master.objects.filter(position='Парикмахер', experience__gt=5)
    return render(request, 'salon/experienced_hairdressers.html', {'masters': masters})

def new_masters_2023(request):
    masters = Master.objects.filter(hire_date__year=2023)
    return render(request, 'salon/new_masters_2023.html', {'masters': masters})

def good_masters(request):
    masters = Master.objects.filter(rating__gte=4.0, rating__lte=4.8)
    return render(request, 'salon/good_masters.html', {'masters': masters})

def hair_services(request):
    services = Service.objects.filter(category='hair')
    return render(request, 'salon/hair_services.html', {'services': services})