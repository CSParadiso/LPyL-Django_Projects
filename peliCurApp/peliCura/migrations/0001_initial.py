# Generated by Django 4.2 on 2023-05-31 14:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, unique=True)),
            ],
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70)),
                ('apellido', models.CharField(max_length=70)),
                ('nombre_artistico', models.CharField(max_length=70)),
                ('nacionalidad', models.CharField(max_length=70)),
                ('foto', models.ImageField(null=True, upload_to='fotos_personas')),
                ('anio_nacimiento', models.IntegerField()),
                ('biografia', models.TextField(max_length=300)),
            ],
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('resumen', models.TextField()),
                ('anio_realizacion', models.IntegerField()),
                ('duracion', models.DurationField()),
                ('puntuacion', models.FloatField(default=0)),
                ('poster', models.ImageField(null=True, upload_to='posters_peliculas')),
                ('actor', models.ManyToManyField(related_name='actor', to='peliCura.persona')),
                ('director', models.ManyToManyField(related_name='director', to='peliCura.persona')),
                ('genero', models.ManyToManyField(to='peliCura.genero')),
            ],
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('E', 'escrito'), ('A', 'publicado'), ('C', 'censurado')], default='E', max_length=1)),
                ('_fecha', models.DateTimeField(auto_now_add=True, verbose_name='%D-%m-%d %H-%M-%S')),
                ('descripcion', models.TextField(max_length=100, verbose_name='Comentario')),
                ('valoracion', models.FloatField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Puntaje')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='peliCura.pelicula')),
            ],
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
