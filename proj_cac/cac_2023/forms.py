from django import forms 
from .models import Mareografo, Detalle_mareog
from django.core.exceptions import ValidationError
from bootstrap_datepicker_plus.widgets import DatePickerInput
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput

SELECTOR_AÑOS = range(1990,2024)

Estaciones = [
    ("Seleccione","Seleccione"),
    ("San_Fernando","San Fernando"),
    ("Palermo","Palermo"),
    ("La_Plata","La Plata"),
    ("Atalaya","Atalaya"),
    ("Santa_Teresita<","Santa Teresita"),
    ("Mar_del_Plata","Mar del Plata"),
    ("Puerto_Belgrano","Puerto Belgrano"),
]

TipoSensor = [
    ("presion","Presion"),
    ("radar","Radar"),
    ("flotador","Flotador"),
]

class ConsultaForm(forms.Form):
    nombre = forms.CharField(label = "Nombre", max_length= 15, required= True)
    apellido = forms.CharField(label = "Apellido", max_length= 15, required= True)
    mail = forms.EmailField(label = "Email", required= True)
    #telefono =   
    
    # todo = forms.CharField()


    # class Meta:

    #     model = Mareografo
    #     fields = ["name", "start_date", "end_date"]
    #     widgets = {
    #         "start_date": DatePickerInput(),
    #         "end_date": DatePickerInput(options={"format": "DD/MM/YYYY"}),
    #     }
    

    est_mar = forms.ChoiceField(
        label= "Estación Mareográfica",
        required= True,
        widget= forms.Select,
        choices = Estaciones,        
    ) 
    # fecha_ini = forms.DateField(label= "Fecha de inicio", required= True,
    #     widget=DatePickerInput(options={"format": "DD/MM/YYYY"}))
    
    # hora_ini = forms.DateField(label="Hora de inicio",required= True,
    #     widget=TimePickerInput(options={"format": "hh:mm"}))


    # fecha_fin = forms.DateField(label= "Fecha fin",required= True,
    #     widget=DatePickerInput(options={"format": "DD/MM/YYYY"})))

    # hora_fin = forms.DateField(label="Hora de fin",required= True,
    #     widget=TimePickerInput(options={"format": "hh:mm"}))
    fecha_ini = forms.DateField(
        label= "Fecha de inicio", 
        required= True,
        widget= forms.SelectDateWidget(years = SELECTOR_AÑOS),
        )
    hora_ini = forms.TimeField(label="Hora de inicio", required= True)
    fecha_fin = forms.DateField(
        label= "Fecha fin", 
        required= True,
        widget= forms.SelectDateWidget(years = SELECTOR_AÑOS),
        )
    hora_fin = forms.TimeField(label="Hora de fin", required= True)
    descr = forms.CharField(
        label='Descripción', 
        widget=forms.Textarea(
        attrs=
        {
        #'class': 'form-control col-12 mb-3',   
        # 'class': 'form-control',
        "placeholder": "Describe el uso que le darás a los datos...",
        "rows":5,
        "cols":50,
        }),)
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['miCampo'].widget.attrs.update({'class': 'form-control mb-3'})
    #     self.fields['descr'].widget.attrs.update({'class': 'form-control'})
 

    # def as_mis_campos(self):
    #     return self._html_output(
    #         normal_row='<div class="col-12 mb-3">{label}{field}{help_text}</div>',
    #         error_row='{errors}',
    #         row_ender='</div>',
    #         help_text_html='<small class="form-text text-muted">{help_text}</small>',
    #         errors_on_separate_row=True
    #     )
                        

class IngresarDatosForm(forms.Form):
    est_mar = forms.ChoiceField(
        label= "Estación Mareográfica",
        required= True,
        widget= forms.Select,
        choices = Estaciones,        
    ) 
    fecha = forms.DateField(
        label= "Fecha", 
        required= True,
        widget= forms.SelectDateWidget(years = SELECTOR_AÑOS),
        )
    hora = forms.TimeField(label="Hora", required= True)
    marea_1 = forms.CharField(label = "Marea_1", max_length= 15)
    marea_2 = forms.CharField(label = "Marea_2", max_length= 15)
    marea_3 = forms.CharField(label = "Marea_3", max_length= 15)
    int_viento = forms.CharField(label = "Intensidad de viento (Nds)", max_length= 15)
    dir_viento = forms.CharField(label = "Dirección de viento (°)", max_length= 15)
    
class EliminarDatosForm(forms.Form):
    est_mar = forms.ChoiceField(
        label= "Estación Mareográfica",
        required= True,
        widget= forms.Select,
        choices = Estaciones,        
    ) 
    fecha = forms.DateField(
        label= "Fecha", 
        required= True,
        widget= forms.SelectDateWidget(years = SELECTOR_AÑOS),
        )
    hora = forms.TimeField(label="Hora", required= True)
    
class altaMareografoForm(forms.ModelForm):
    class Meta:
        model = Mareografo 
        fields = "__all__"
 
    
class DetalleMareografoForm(forms.ModelForm):
    class Meta:
        model = Detalle_mareog
        fields = "__all__"    
    
"""class altaMareografoForm(forms.Form):    
    est_mar = forms.CharField(label = "Nombre de Estacion", max_length= 15, required= True)
    tipo = forms.ChoiceField(
        label= "Tipo de sensor",
        required= True,
        widget= forms.Select,
        choices = TipoSensor,        
    )
    marca = forms.CharField(label = "Marca sensor", max_length= 15, required= True)
    modelo = forms.CharField(label = "Modelo", max_length= 15, required= True)
    s_n = forms.CharField(label = "Num de serie", max_length= 15, required= True)
"""    
    