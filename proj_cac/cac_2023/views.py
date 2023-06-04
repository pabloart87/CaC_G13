from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .forms import ConsultaForm, IngresarDatosForm, EliminarDatosForm, altaMareografoForm
from .models import Mareografo

@login_required
def alta_mareografo(request):
    if request.method == "POST":
        alta_form = altaMareografoForm(request.POST)
        if alta_form.is_valid():
            
            mareografo_nuevo = Mareografo(
                nombre = alta_form.cleaned_data["est_mar"],
                tipo = alta_form.cleaned_data["tipo"],
                marca = alta_form.cleaned_data["marca"],
                modelo = alta_form.cleaned_data["modelo"],
                s_n = alta_form.cleaned_data["s_n"],
            )
            
            mareografo_nuevo.save()
            
            messages.add_message(request, messages.SUCCESS, "Mareógrafo dado de alta exitosamente", extra_tags="tag1")
            
            return redirect("inicio")
    else:
        alta_form = altaMareografoForm()
    
    context = {"form": alta_form}
        
    return render(request, "cac_2023/alta_mareografo.html", context)

@login_required
def ingreso_datos(request):
    if request.method == "POST":
        ingreso_form = IngresarDatosForm(request.POST)
        if ingreso_form.is_valid():
                        
            messages.add_message(request, messages.SUCCESS, "Ingreso de dato exitoso", extra_tags="tag1")
            
            return redirect("inicio")
    else:
        ingreso_form = IngresarDatosForm()
    
    context = {"form": ingreso_form}
        
    return render(request, "cac_2023/ingreso_datos.html", context)

@login_required
def eliminar_datos(request):
    if request.method == "POST":
        eliminar_form = EliminarDatosForm(request.POST)
        if eliminar_form.is_valid():
                       
            messages.add_message(request, messages.SUCCESS, "Se eliminó el dato exitosamente", extra_tags="tag1")
            
            return redirect("inicio")
    else:
        eliminar_form = EliminarDatosForm()
    
    context = {"form": eliminar_form}
        
    return render(request, "cac_2023/eliminar_datos.html", context)

# def calcular_edad(request, edad, agno):
#     periodo = agno - 2023
#     edad_futura = edad + periodo
#     documento = "<html><body><h1>En el año %s tendrás %s años"% (agno, edad_futura)
#     return HttpResponse(documento) 


"""def lista_mareografos(request):
    
    context = {}
    
    listado = Mareografo.objects.all()
    
    context["lista_mareografos"] = listado
    return render(request, "cac_2023/lista_mareografos.html", context)"""

class lista_mareografos(ListView):
    model = Mareografo
    context_object_name = "Mareógrafos"
    template_name = "cac_2023/lista_mareografos.html"
    ordering = ["nombre"]


def consulta(request):
    if request.method == "POST":
        consulta_form = ConsultaForm(request.POST)
        if consulta_form.is_valid():
            
            
            messages.add_message(request, messages.SUCCESS, "Consulta enviada con éxito", extra_tags="tag1")
            
            return redirect("inicio")
    else:
        consulta_form = ConsultaForm()
    
    context = {"form": consulta_form}

    return render(request, "cac_2023/consulta.html", context)
    
def inicio(request):
    
    context = {}
    
    return render(request, "cac_2023/index.html", context )

def login(request):
    
    context = {}
    
    return render(request, "cac_2023/login.html", context )
