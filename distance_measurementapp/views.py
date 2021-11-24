from django.shortcuts import render, get_object_or_404
from .models import Measurement
from .forms import MeasurementModelForm
from geopy.geocoders import Nominatim

# Create your views here.

def distance_calculation_view(request):
    obj = get_object_or_404(Measurement, id=1)
    form = MeasurementModelForm(request.POST or None)
    geolocator = Nominatim(user_agent='distance_measurementapp')

    if form.is_valid():
        instance = form.save(commit=False)
        destination_place = form.cleaned_data.get('destination')
        destination = geolocator.geocode(destination_place)
        print(destination)
        dest_lati = destination.latitude
        dest_long = destination.longitude

        instance.location = 'Bangalore'
        instance.distance = 70.00 
        #instance.save()

    context = {
        'distance' : obj,
        'form' : form,
    }
    return render(request, 'main.html', context)

