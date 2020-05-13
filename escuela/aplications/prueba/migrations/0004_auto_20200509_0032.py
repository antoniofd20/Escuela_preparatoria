# Generated by Django 3.0.6 on 2020-05-09 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0003_auto_20200509_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='celular',
            field=models.CharField(max_length=10, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='tel_recado',
            field=models.CharField(max_length=10, verbose_name='Telefono de contacto'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='telefono',
            field=models.CharField(max_length=10, verbose_name='Telefono de casa'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='celular',
            field=models.CharField(max_length=10, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='tel_recado',
            field=models.CharField(max_length=10, verbose_name='Telefono de contacto'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='telefono',
            field=models.CharField(max_length=10, verbose_name='Telefono de casa'),
        ),
    ]
