from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= "index"),
    path('ingresar_datos', views.ingreso_datos, name= "ingresar_datos"),
    path('eliminar_datos', views.eliminar_datos, name= "eliminar_datos"),
    path('calcular_edad/<int:edad>/<int:agno>', views.calcular_edad, name= "calcular_edad" ),
    path("lista_mareografos", views.lista_mareografos.as_view(), name="lista_mareografos"),
    path("consulta", views.consulta, name="consulta"),
    path("inicio", views.inicio, name="inicio"),
    path("alta_mareografo", views.alta_mareografo, name="alta_mareografo"),
]

