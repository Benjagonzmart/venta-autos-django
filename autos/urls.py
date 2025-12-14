from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_autos, name="lista_autos"),
    path("<int:id>/", views.detalle_auto, name="detalle_auto"),
]