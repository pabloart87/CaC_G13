from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hola mundo django 2023!!!")

def ingreso_datos(request):
    return HttpResponse("INGRESO DE DATOS")

def eliminar_datos(request):
    return HttpResponse("ELIMINAR DATOS")

def calcular_edad(request, edad, agno):
    periodo = agno - 2023
    edad_futura = edad + periodo
    documento = "<html><body><h1>En el año %s tendrás %s años"% (agno, edad_futura)
    return HttpResponse(documento) 

def index2(request):
    return render(request, "index2.html")

def consulta(request):
    return render(request, "consulta.html")

def inicio(request):
    return render(request, "inicio.html")