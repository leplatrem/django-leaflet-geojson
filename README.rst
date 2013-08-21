Example project of `Geodjango maps with Leaflet <http://blog.mathieu-leplatre.info/geodjango-maps-with-leaflet.html>`_

=======
INSTALL
=======

Install project dependencies :

    virtualenv env
    source env/bin/activate

    python setup.py develop


On Ubuntu, I use these commands to install Spatialite :

::

    sudo apt-add-repository -y ppa:ubuntugis/ppa
    sudo apt-get update > /dev/null

    sudo apt-get install libgdal-dev libproj-dev libgeos-dev libspatialite-dev spatialite-bin

And it python module *pysqlite* :

::

    wget http://pysqlite.googlecode.com/files/pysqlite-2.6.3.tar.gz
    tar -zxvf pysqlite-2.6.3.tar.gz
    cd pysqlite-2.6.3
    sed -i "s/define=SQLITE_OMIT_LOAD_EXTENSION//g" setup.cfg
    python setup.py install
    cd .. 


=========
LOAD DATA
=========

Initialize Spatialite DB :

::

    spatialite database.db "SELECT InitSpatialMetaData();"

::

    python manage.py syncdb


Load all weather station instances from GeoJSON :

::

    python manage.py shell

    >>> from django.core.serializers import deserialize
    >>> 
    >>> source = open('Pub9volA130819x.geojson')
    >>> for ws in deserialize('geojson', source):
    ...     ws.save()


======
PLAY !
======

::

    python manage.py runserver


Have a look at those 12 000 markers ! (ouch, you hear that ? That's your CPU fan...)
