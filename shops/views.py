from .models import Shop
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.gis.measure import D
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point

from .forms import LocationForm
# Create your views here.

@require_http_methods(["GET", "POST"])
def shop_list(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = LocationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            longitude = form.cleaned_data["longitude"]
            latitude = form.cleaned_data["latitude"]
            distance = form.cleaned_data["distance"]
            user_point = Point(longitude, latitude)
            shops = (
                Shop.objects.filter(
                    location__distance_lt=(
                        user_point,
                        D(km=distance)
                    )
                ).annotate(
                    distance=Distance(
                        'location',
                        user_point
                    )
                )
                .order_by('distance')
                .values()
            )
            return render(request, "shop_list.html", {"form": form,"shops": shops})
        else:
            return HttpResponseRedirect("/")
    else:
        form = LocationForm()
    return render(request, "shop_list.html", {"form": form})