from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin

from .models import WeatherStation, Region


admin.site.register(WeatherStation, LeafletGeoAdmin)
admin.site.register(Region, LeafletGeoAdmin)
