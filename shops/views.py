from .models import Shop
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.gis.measure import D
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point

from .forms import LocationForm, ShopForm, ShopDetailForm
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
            print(form.errors)
            return redirect("/")
    else:
        form = LocationForm()
    return render(request, "shop_list.html", {"form": form})

@require_http_methods(["GET", "POST"])
def home_view(request):
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
    form = ShopForm()
    shops = Shop.objects.all()
    return render(request, 'home.html', {'form': form, "shops": shops})

@require_http_methods(["GET"])
def detail_view(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    form = ShopDetailForm(instance=shop)
    return render(request, 'detail.html', {'shop': shop, 'form': form})

@require_http_methods(["GET", "POST"])
def update_view(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    if request.method == 'POST':
        form = ShopForm(request.POST, instance=shop)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ShopForm(instance=shop)
    return render(request, 'update.html', {'form': form, 'shop': shop})

@require_http_methods(["GET", "POST"])
def delete_view(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    if request.method == 'POST':
        shop.delete() # in realworl we can use soft deletion
        return redirect('/')
    return render(request, 'delete.html', {'shop': shop})