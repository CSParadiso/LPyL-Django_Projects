# Generated by Django 4.2 on 2023-05-31 20:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliCura', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='duracion',
            field=models.DurationField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1240)]),
        ),
    ]