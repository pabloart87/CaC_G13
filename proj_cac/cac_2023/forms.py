from django import forms 

SELECTOR_AÑOS = range(1990,2024)

Estaciones = [
    ("San_Fernando","San Fernando"),
    ("Palermo","Palermo"),
    ("La_Plata","La Plata"),
    ("Atalaya","Atalaya"),
    ("Santa_Teresita<","Santa Teresita"),
    ("Mar_del_Plata","Mar del Plata"),
    ("Puerto_Belgrano","Puerto Belgrano"),
]

class ConsultaForm(forms.Form):
    nombre = forms.CharField(label = "Nombre", max_length= 15, required= True)
    apellido = forms.CharField(label = "Apellido", max_length= 15, required= True)
    mail = forms.EmailField(label = "Email", required= True)
    #telefono = 
    est_mar = forms.ChoiceField(
        label= "Estación Mareográfica",
        required= True,
        widget= forms.Select,
        choices = Estaciones,        
    ) 
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
    descr = forms.CharField(widget=forms.Textarea, label= "Describe el uso que le darás a los datos")
    