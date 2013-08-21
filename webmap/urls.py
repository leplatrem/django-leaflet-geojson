from django.views.generic import TemplateView
from django.conf.urls import patterns, url

from djgeojson.views import GeoJSONLayerView

from .models import WeatherStation


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=WeatherStation), name='data')
)
