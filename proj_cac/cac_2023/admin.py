from django.contrib import admin
from .models import Mareografo, Detalle_mareog, Datos_sensores, Sensor_hidrostatico

admin.site.register(Mareografo)
admin.site.register(Detalle_mareog)
admin.site.register(Datos_sensores)
admin.site.register(Sensor_hidrostatico)

