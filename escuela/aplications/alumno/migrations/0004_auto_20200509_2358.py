# Generated by Django 3.0.6 on 2020-05-10 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0003_auto_20200509_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='sexo',
            field=models.CharField(max_length=10, verbose_name='Sexo'),
        ),
    ]
