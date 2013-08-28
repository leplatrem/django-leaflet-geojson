from django.db import models
from django.contrib.gis.db import models as gismodels


class WeatherStation(gismodels.Model):

    wmoid = models.IntegerField()
    name = models.CharField(max_length=256)

    geom = gismodels.PointField()

    objects = gismodels.GeoManager()

    def __unicode__(self):
        return self.name


class Region(gismodels.Model):

    name = models.CharField(max_length=256)

    geom = gismodels.PolygonField()

    objects = gismodels.GeoManager()

    def __unicode__(self):
        return self.name
