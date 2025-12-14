from django.shortcuts import render , get_object_or_404
from .models import Auto


def lista_autos(request):
    autos = Auto.objects.all()
    return render(request, "autos/lista_autos.html", {"autos": autos})
# Create your views here.

def detalle_auto(request, id):
    auto = get_object_or_404(Auto, id=id)
    return render(request, "autos/detalle_auto.html", {"auto": auto})