# Generated by Django 4.2.1 on 2023-05-22 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mareografo',
            fields=[
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('tipo', models.CharField(max_length=50, verbose_name='Tipo')),
                ('marca', models.CharField(max_length=50, verbose_name='Marca')),
                ('modelo', models.CharField(max_length=50, verbose_name='Modelo')),
                ('s_n', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='S/N')),
            ],
        ),
        migrations.CreateModel(
            name='Datos_sensores',
            fields=[
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('hora', models.TimeField(verbose_name='Hora')),
                ('marea_1', models.IntegerField(verbose_name='Marea 1')),
                ('marea_2', models.IntegerField(verbose_name='Marea 2')),
                ('marea_3', models.IntegerField(verbose_name='Marea 3')),
                ('intensidad_viento', models.IntegerField(verbose_name='Intensidad de viento')),
                ('direccion_viento', models.IntegerField(verbose_name='Dirección de viento')),
                ('mareografo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cac_2023.mareografo')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_mareog',
            fields=[
                ('ubicacion', models.CharField(max_length=50, verbose_name='Ubicación')),
                ('posicion', models.CharField(max_length=50, verbose_name='Posición')),
                ('nombre_contacto', models.CharField(max_length=50, verbose_name='Nombre contacto')),
                ('tel_contacto', models.IntegerField(verbose_name='Teléfono de contacto')),
                ('mareografo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cac_2023.mareografo')),
            ],
        ),
        migrations.CreateModel(
            name='Sensor_hidrostatico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=8, verbose_name='Tipo de sensor')),
                ('mareografo', models.ManyToManyField(to='cac_2023.mareografo')),
            ],
        ),
    ]
