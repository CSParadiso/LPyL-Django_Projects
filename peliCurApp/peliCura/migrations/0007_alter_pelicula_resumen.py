# Generated by Django 4.2 on 2023-05-31 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliCura', '0006_alter_pelicula_resumen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='resumen',
            field=models.TextField(max_length=200, verbose_name='Resumen'),
        ),
    ]
