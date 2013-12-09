from django import forms
from django.views.generic import UpdateView
from django.core.urlresolvers import reverse

from .models import WeatherStation
from leaflet.forms.fields import PointField


class WeatherStationForm(forms.ModelForm):
    geom = PointField()
    class Meta:
        model = WeatherStation


class EditWeatherStation(UpdateView):
    model = WeatherStation
    form_class = WeatherStationForm
    template_name = 'form.html'

    def get_success_url(self):
        return reverse('home')
