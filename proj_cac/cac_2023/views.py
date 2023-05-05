from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hola mundo django 2023!!!")

def ingreso_datos(request):
    context = {}
    return render(request, "cac_2023/ingreso_datos.html", context)

def eliminar_datos(request):
    context = {}
    return render(request, "cac_2023/eliminar_datos.html", context)

def calcular_edad(request, edad, agno):
    periodo = agno - 2023
    edad_futura = edad + periodo
    documento = "<html><body><h1>En el año %s tendrás %s años"% (agno, edad_futura)
    return HttpResponse(documento) 

def index2(request):
    
    alumno_ficticio = {
        "name" : "Bianca",
        "last_name" : "Concatti",
        "age" : 26,
        "valid" : False
    }
    
    listado_alumnos = [ 
    {
        "name" : "Bianca",
        "last_name" : "Concatti",
        "age" : 26,
        "valid" : False
    },
    {
        "name" : "Martin",
        "last_name" : "El martu",
        "age" : 26,
        "valid" : False
    },
    {
        "name" : "Cheba",
        "last_name" : "El pancho",
        "age" : 26,
        "valid" : False
    },
    {
        "name" : "La",
        "last_name" : "Lola",
        "age" : 26,
        "valid" : False
    },
    ]
    
    context = {
        "name": "Pablo",
        "last_name": "Toledo",
        "alumn": alumno_ficticio,
        "listado_alumnos": listado_alumnos
        }
    
    return render(request, "cac_2023/index2.html", context)

def consulta(request):
    
    context = {}
    
    return render(request, "cac_2023/consulta.html", context)

def inicio(request):
    
    context = {}
    
    return render(request, "cac_2023/inicio.html", context )