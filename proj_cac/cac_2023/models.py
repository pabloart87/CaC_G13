from django.db import models

class Mareografo(models.Model):
    TipoSensor = (
        ("PRESION","Presion"),
        ("RADAR","Radar"),
        ("FLOTADOR","Flotador"),
    )
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    tipo = models.CharField(max_length=8, choices = TipoSensor)
    marca = models.CharField(max_length=50, verbose_name="Marca")
    modelo = models.CharField(max_length=50, verbose_name="Modelo")
    s_n = models.CharField(max_length=50, verbose_name="S/N", primary_key=True)
    
class Detalle_mareog(models.Model):
    ubicacion = models.CharField(max_length=50, verbose_name="Ubicación")
    posicion = models.CharField(max_length=50, verbose_name="Posición", help_text="Formato: GG MM,MMMM GGG MM,MMMM ")
    nombre_contacto = models.CharField(max_length=50, verbose_name="Nombre contacto")
    tel_contacto = models.IntegerField(verbose_name="Teléfono de contacto", help_text="Sin 0 y sin 15")
    mareografo = models.OneToOneField(Mareografo, on_delete=models.CASCADE, primary_key=True) #Uno a Uno
    
class Datos_sensores(models.Model):
    fecha = models.DateField(verbose_name="Fecha", help_text="Formato: DD/MM/AAAA")
    hora = models.TimeField(verbose_name="Hora", help_text="Formato: HH:MM")
    marea_1 = models.IntegerField(verbose_name="Marea 1")
    marea_2 = models.IntegerField(verbose_name="Marea 2")
    marea_3 = models.IntegerField(verbose_name="Marea 3")
    intensidad_viento = models.IntegerField(verbose_name="Intensidad de viento")
    direccion_viento = models.IntegerField(verbose_name="Dirección de viento")
    mareografo = models.OneToOneField(Mareografo, on_delete=models.CASCADE, primary_key=True) #Uno a Uno
    
class Sensor_hidrostatico(models.Model):
    tipo = models.CharField(max_length=8, verbose_name="Tipo de sensor")
    mareografos = models.ManyToManyField(Mareografo) #Muchos a Muchos
    