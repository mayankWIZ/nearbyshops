from django import forms
from django.contrib.gis import forms as geo_forms
from .models import Shop

class LocationForm(forms.Form):
    longitude = forms.FloatField(label="Longitude", min_value=-90.00000000, max_value=90.00000000, required=True)
    latitude = forms.FloatField(label="Latitude", min_value=-180.00000000, max_value=180.00000000, required=True)
    distance = forms.FloatField(label="Distance (in kilometers)", min_value=0, required=True)

class ShopForm(forms.ModelForm):
    location = geo_forms.PointField(
        srid=4326,
        widget=geo_forms.OSMWidget(
            attrs={
                "map_srid": 4326,
                "default_lon": 78.8718,
                "default_lat": 21.7679,
                "default_zoom": 8,
            }
        )
    )
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.location = instance.location.wkt
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Shop
        fields = "__all__"

class ShopDetailForm(forms.ModelForm):
    name = forms.CharField(disabled=True)
    address = forms.CharField(disabled=True)
    city = forms.CharField(disabled=True)
    location = geo_forms.PointField(
        widget=geo_forms.OSMWidget(
            attrs={
                "map_srid": 4326,
                "default_lon": 78.8718,
                "default_lat": 21.7679,
                "default_zoom": 8
            }
        ),
        disabled=True
    )

    class Meta:
        model = Shop
        fields = "__all__"