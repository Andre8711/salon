
from django.shortcuts import render
from .models import Salon

def active_salons(request):
    salons = Salon.objects.filter(is_active=True)
    return render(request, 'salon/active_salons.html', {'salons': salons})