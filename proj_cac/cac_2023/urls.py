from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= "index"),
    path('ingresar_datos', views.ingreso_datos, name= "ingresar_datos"),
    path('eliminar_datos', views.eliminar_datos, name= "eliminar_datos"),
    path('calcular_edad/<int:edad>/<int:agno>', views.calcular_edad, name= "calcular_edad" ),
    path("index2", views.index2, name="index2"),
    path("consulta", views.consulta, name="consulta"),
    path("inicio", views.inicio, name="inicio"),
]

