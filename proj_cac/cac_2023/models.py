from django.db import models

class Sensor_hidrostatico(models.Model):
    class Meta:
        verbose_name_plural = ("SENSOR HIDROSTÁTICO")
    
    """TipoSensor = (
        ("PRESION","Presion"),
        ("RADAR","Radar"),
        ("FLOTADOR","Flotador"),
    )"""
    tipo = models.CharField(max_length=8, verbose_name="Tipo de sensor")
    #mareografos = models.ManyToManyField(Mareografo) #Muchos a Muchos
    
    def __str__(self):
        return f"{self.tipo}"


class Mareografo(models.Model):
    class Meta:
        verbose_name_plural = ("MAREÓGRAFOS")

    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    marca = models.CharField(max_length=50, verbose_name="Marca")
    modelo = models.CharField(max_length=50, verbose_name="Modelo")
    s_n = models.CharField(max_length=50, verbose_name="S/N", primary_key=True)
    sensores = models.ManyToManyField(Sensor_hidrostatico, related_name="sensores")

    def __str__(self):
        return f"{self.nombre} | S/N: {self.s_n} |"
    
    
class Detalle_mareog(models.Model):
    class Meta:
        verbose_name_plural = ("DETALLE MAREÓGRAFOS")

    ubicacion = models.CharField(max_length=50, verbose_name="Ubicación")
    posicion = models.CharField(max_length=50, verbose_name="Posición", help_text="Formato: GG MM,MM (X) GGG MM,MM (X) ")
    nombre_contacto = models.CharField(max_length=50, verbose_name="Nombre contacto")
    tel_contacto = models.IntegerField(verbose_name="Teléfono de contacto", help_text="Sin 0 y sin 15")
    mareografo = models.OneToOneField(Mareografo, on_delete=models.CASCADE, primary_key=True) #Uno a Uno

    def __str__(self):
        return f"{self.mareografo} |  {self.ubicacion} |  {self.posicion} |"
    
    
class Datos_sensores(models.Model):
    class Meta:
        verbose_name_plural = ("DATOS SENSORES")

    fecha = models.DateField(verbose_name="Fecha", help_text="Formato: DD/MM/AAAA")
    hora = models.TimeField(verbose_name="Hora", help_text="Formato: HH:MM")
    marea_1 = models.IntegerField(verbose_name="Marea 1")
    marea_2 = models.IntegerField(verbose_name="Marea 2")
    marea_3 = models.IntegerField(verbose_name="Marea 3")
    intensidad_viento = models.IntegerField(verbose_name="Intensidad de viento")
    direccion_viento = models.IntegerField(verbose_name="Dirección de viento")
    mareografo = models.OneToOneField(Mareografo, on_delete=models.CASCADE, primary_key=True) #Uno a Uno
    
    

    
    
    