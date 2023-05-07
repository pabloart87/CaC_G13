from django import forms 

class ConsultaForm(forms.Form):
    nombre = forms.CharField(label = "Nombre: ", max_length= 15, required= True)
    apellido = forms.CharField(label = "Apellido: ", max_length= 15, required= True)
    mail = forms.EmailField(label = "Email: ", required= True)
    #telefono = 
    #est_mar =
    fecha_ini = forms.DateField(label= "Fecha de inicio: ", required= True)
    hora_ini = forms.TimeField(label="Hora de inicio", required= True)
    fecha_fin = forms.DateField(label= "Fecha de fin: ", required= True)
    hora_fin = forms.TimeField(label="Hora de fin", required= True)
    #descr =
    