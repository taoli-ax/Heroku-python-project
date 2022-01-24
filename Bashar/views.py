from django.shortcuts import render
from .models import Shipper


# Create your views here.
def index_bashar(request):
    ships = Shipper.objects.all()
    context = {'ships': ships}
    return render(request, 'BasharIntro.html', context=context)


def ship_detail(request,pk):
    ship=Shipper.objects.get(pk=pk)
    context={'ship':ship}
    return render(request, 'BasharIntro_detail.html', context=context)
