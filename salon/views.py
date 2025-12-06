
from django.shortcuts import render, get_object_or_404
from .models import Salon
from .models import Master
from .models import Service
from .models import MasterService

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


def budget_services(request):
    services = Service.objects.filter(price__lt=2000, duration__gt=30)
    return render(request, 'salon/budget_services.html', {'services': services})

def haircut_services(request):
    services = Service.objects.filter(name__icontains='стрижка')
    return render(request, 'salon/haircut_services.html', {'services': services})

def salon_masters(request, salon_id):
    salon = get_object_or_404(Salon, id=salon_id)
    masters = salon.master_set.prefetch_related('masterservice_set__service')
    return render(request, 'salon/salon_masters.html', {'salon': salon, 'masters': masters})

def master_services(request, master_id):
    master = get_object_or_404(Master, id=master_id)
    services = master.masterservice_set.select_related('service')
    return render(request, 'salon/master_services.html', {'master': master, 'services': services})


def salons_with_cosmetologists(request):
    salons = Salon.objects.filter(master__specialization='cosmetology').distinct()
    return render(request, 'salon/salons_with_cosmetologists.html', {'salons': salons})

def expensive_service_masters(request):
    masters = Master.objects.filter(masterservice__service__price__gt=3000).distinct()
    return render(request, 'salon/expensive_service_masters.html', {'masters': masters})

def discounted_services(request):
    services = MasterService.objects.filter(special_price__isnull=False).select_related('service', 'master')
    return render(request, 'salon/discounted_services.html', {'services': services})