# Generated by Django 4.1.7 on 2023-06-05 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cac_2023', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datos_sensores',
            options={'verbose_name_plural': 'DATOS SENSORES'},
        ),
        migrations.AlterModelOptions(
            name='detalle_mareog',
            options={'verbose_name_plural': 'DETALLE MAREÓGRAFOS'},
        ),
        migrations.AlterModelOptions(
            name='mareografo',
            options={'verbose_name_plural': 'MAREÓGRAFOS'},
        ),
        migrations.AlterModelOptions(
            name='sensor_hidrostatico',
            options={'verbose_name_plural': 'SENSOR HIDROSTÁTICO'},
        ),
        migrations.RenameField(
            model_name='sensor_hidrostatico',
            old_name='mareografo',
            new_name='mareografos',
        ),
        migrations.RemoveField(
            model_name='mareografo',
            name='tipo',
        ),
        migrations.AlterField(
            model_name='datos_sensores',
            name='fecha',
            field=models.DateField(help_text='Formato: DD/MM/AAAA', verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='datos_sensores',
            name='hora',
            field=models.TimeField(help_text='Formato: HH:MM', verbose_name='Hora'),
        ),
        migrations.AlterField(
            model_name='detalle_mareog',
            name='posicion',
            field=models.CharField(help_text='Formato: GG MM,MM (X) GGG MM,MM (X) ', max_length=50, verbose_name='Posición'),
        ),
        migrations.AlterField(
            model_name='detalle_mareog',
            name='tel_contacto',
            field=models.IntegerField(help_text='Sin 0 y sin 15', verbose_name='Teléfono de contacto'),
        ),
        migrations.AlterField(
            model_name='sensor_hidrostatico',
            name='tipo',
            field=models.CharField(choices=[('PRESION', 'Presion'), ('RADAR', 'Radar'), ('FLOTADOR', 'Flotador')], max_length=8, verbose_name='Tipo de sensor'),
        ),
    ]
