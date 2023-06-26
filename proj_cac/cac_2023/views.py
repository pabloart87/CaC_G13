from typing import Any, Dict
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponseRedirect
from django.views.generic import ListView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib import messages
from .forms import ConsultaForm, IngresarDatosForm, EliminarDatosForm, altaMareografoForm, DetalleMareografoForm, TipoSensorForm
from .models import Mareografo, Detalle_mareog

@login_required
@permission_required("cac_2023.add_mareografo")
def alta_mareografo(request):
    if request.method == "POST":
        alta_form = altaMareografoForm(request.POST)
        if alta_form.is_valid():
                       
            alta_form.save()
            
            messages.add_message(request, messages.SUCCESS, "Mareógrafo dado de alta exitosamente", extra_tags="tag1")
            
            return redirect("detalle_mareografos")
    else:
        alta_form = altaMareografoForm()
    
    context = {"form": alta_form}
        
    return render(request, "cac_2023/alta_mareografo.html", context)


@login_required
def detalle_mareografos(request):
    if request.method == "POST":
        detalle_form = DetalleMareografoForm(request.POST)
        if detalle_form.is_valid():
            
            detalle_form.save()
            
            messages.add_message(request, messages.SUCCESS, "Detalle de mareógrafo guardado", extra_tags="tag1")
            
            return redirect("inicio")
    else:
        detalle_form = DetalleMareografoForm()
    
    context = {"form": detalle_form}
        
    return render(request, "cac_2023/detalle_mareografos.html", context)

@login_required
@permission_required("cac_2023.add_mareografo")
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
@permission_required("cac_2023.add_mareografo")
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

class lista_mareografos(ListView):
    model = Mareografo
    context_object_name = "Mareógrafos"
    template_name = "cac_2023/lista_mareografos.html"
    ordering = ["nombre"]

class ver_detalles(ListView):
    model = Detalle_mareog
    context_object_name = "Detalles"
    template_name = "cac_2023/ver_detalles.html"
    ordering = ["mareografo"]

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

def logout(request):
    
    context = {}
    
    return render(request, "cac_2023/index.html", context )
