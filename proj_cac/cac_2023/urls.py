from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.inicio, name= "inicio"),
    path('ingresar_datos', views.ingreso_datos, name= "ingresar_datos"),
    path('eliminar_datos', views.eliminar_datos, name= "eliminar_datos"),
    # path('calcular_edad/<int:edad>/<int:agno>', views.calcular_edad, name= "calcular_edad" ),
    path("lista_mareografos", views.lista_mareografos.as_view(), name="lista_mareografos"),
    path("consulta", views.consulta, name="consulta"),
    path("inicio", views.inicio, name="inicio"),
    path("alta_mareografo", views.alta_mareografo, name="alta_mareografo"),
    #path("login", views.login, name="login"),
    #path('', TemplateView.as_view(template_name="cac_2023/login.html")),
    # path('account/login/',auth_views.LoginView.as_view(template_name='cac_2023/login.html'), name='login'),
    # path('accounts/', include('allauth.urls')),
    
]
