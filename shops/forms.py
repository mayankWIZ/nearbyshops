from django import forms

class LocationForm(forms.Form):
    longitude = forms.FloatField(label="Longitude", min_value=-90.00000000, max_value=90.00000000, required=True)
    latitude = forms.FloatField(label="Latitude", min_value=-180.00000000, max_value=180.00000000, required=True)
    distance = forms.FloatField(label="Distance (in kilometers)", min_value=0, required=True)