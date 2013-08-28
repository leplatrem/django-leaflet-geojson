import os

PROJECT_PATH = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG
SECRET_KEY = os.getenv("SECRET_KEY", 'booh')
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", '*')

STATIC_URL = '/static/'

ROOT_URLCONF = 'webmap.urls'

TEMPLATE_DIRS = (PROJECT_PATH,)

INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'leaflet',
    'djgeojson',
    'webmap',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': os.path.join(PROJECT_PATH, '..', 'database.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

SERIALIZATION_MODULES = {
    'geojson': 'djgeojson.serializers'
}

LEAFLET_CONFIG = {
    'PLUGINS': {
        'leaflet.spin': {
            'js': ['http://fgnass.github.io/spin.js/dist/spin.min.js',
                   'http://makinacorpus.github.io/Leaflet.Spin/leaflet.spin.js']
        }
    }
}