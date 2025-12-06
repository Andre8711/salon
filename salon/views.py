
from django.shortcuts import render, get_object_or_404
from .models import Salon


def active_salons(request):
    salons = Salon.objects.filter(is_active=True)
    return render(request, 'salon/active_salons.html', {'salons': salons})
    

def salon_detail(request, salon_id):
    salon = get_object_or_404(Salon, id=salon_id)
    return render(request, 'salon/salon_detail.html', {'salon': salon})