# Generated by Django 5.0.1 on 2024-04-29 21:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_buque', models.TextField(max_length=20)),
                ('horometro', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_departamento', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_equipo', models.TextField(max_length=20)),
                ('hora_standar', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Equipos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_equipo', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sistema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_sistema', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.TextField(max_length=20)),
                ('password_usuario', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_texto', models.TextField(max_length=300)),
                ('nombre_prioridad', models.TextField(max_length=20)),
                ('ultimo_mantenimiento', models.DateField()),
                ('ultimo_horometro', models.IntegerField()),
                ('comentario', models.TextField(max_length=500)),
                ('estado_ejecucion', models.TextField(max_length=50)),
                ('buque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buques.buque')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buques.departamento')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buques.equipo')),
                ('sistema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buques.sistema')),
            ],
        ),
        migrations.CreateModel(
            name='HistorialCal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_actividad', models.TextField(max_length=200)),
                ('descripcion_frecuencia', models.IntegerField()),
                ('fecha_historial', models.DateTimeField()),
                ('buque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buques.buque')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buques.departamento')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buques.equipo')),
                ('sistema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buques.sistema')),
            ],
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_historial', models.TextField(max_length=200)),
                ('registro_horometro', models.IntegerField()),
                ('fecha_hora_historial', models.DateTimeField()),
                ('buque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buques.buque')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buques.departamento')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buques.equipo')),
                ('sistema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buques.sistema')),
            ],
        ),
        migrations.CreateModel(
            name='Fecha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actividad', models.TextField(max_length=50)),
                ('prioridad', models.TextField(max_length=50)),
                ('ult_mantenimiento', models.DateField(max_length=50)),
                ('texto_comentario', models.TextField(max_length=500)),
                ('ejecucion', models.TextField(max_length=50)),
                ('frecuencia', models.IntegerField()),
                ('buque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buques.buque')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buques.departamento')),
                ('equipos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buques.equipos')),
                ('sistema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buques.sistema')),
            ],
        ),
    ]
