from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from taxi.models import Manufacturer, Car, Driver


def index(request: HttpRequest) -> HttpResponse:
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()
    context = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars,
    }
    return render(request, template_name="taxi/index.html", context=context)
