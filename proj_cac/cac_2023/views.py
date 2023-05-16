from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AltaUsuarioForm, EnviarConsultaForm

# Create your views here.
def index(request):
    return HttpResponse("hola mundo django 2023!!!")

# def ingreso_datos(request):
#     context = {}
#     return render(request, "cac_2023/ingreso_datos.html", context)

def ingreso_datos(request):

    if request.method == "POST":

        alta_usuario_form = AltaUsuarioForm(request.POST)

    else:

        alta_usuario_form = AltaUsuarioForm()

    context = {
        'form' : alta_usuario_form
        }
    
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

    if request.method == "POST":
        form = EnviarConsultaForm(request.POST)
        if form.is_valid():
            print("------------------------")
            print(form.cleaned_data['mail'])

            messages.add_message(request, messages.SUCCESS, 'Consulta enviada con exito', extra_tags="tag1")

            # Usualmente cuando se completa exitosamente un formulario
            # redirijimos al usuario a otra parte del sitio (por ejemplo al index)
            # para que no intente enivar dos veces el mismo formulario.
            return redirect("index2")
    else:
        # GET
        form = EnviarConsultaForm()

    context = {'form': form}

    return render(request, "cac_2023/consulta.html", context)


def inicio(request):
    
    context = {}
    
    return render(request, "cac_2023/inicio.html", context )