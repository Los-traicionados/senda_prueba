# Generated by Django 4.0.4 on 2023-11-10 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('act_nombre', models.CharField(help_text='Andar a Caballo, Caminata guiada...', max_length=50, verbose_name='Nombre de la Actividad')),
                ('act_descripcion', models.CharField(max_length=255, verbose_name='Descripción de la actividad')),
                ('act_precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio actividad')),
                ('act_imagen', models.ImageField(default='', upload_to='actividad/')),
            ],
            options={
                'verbose_name_plural': 'Actividades',
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ho_nombre', models.CharField(max_length=50, verbose_name='Hotel')),
                ('ho_direccion', models.CharField(max_length=255, verbose_name='Dirección')),
                ('ho_precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio Hotel')),
                ('ho_ciudad', models.CharField(blank=True, max_length=50, null=True)),
                ('ho_imagen', models.ImageField(blank=True, default='', null=True, upload_to='hotel/')),
            ],
            options={
                'verbose_name_plural': 'Hoteles',
            },
        ),
        migrations.CreateModel(
            name='Pack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pa_nombre', models.CharField(max_length=50, verbose_name='Nombre del Pack')),
                ('pa_descipcion', models.CharField(max_length=255, verbose_name='Descripción Pack')),
                ('pa_imagen', models.ImageField(default='', upload_to='pack/')),
            ],
            options={
                'verbose_name_plural': 'Packs',
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res_f_inicio', models.DateTimeField(blank=True, null=True)),
                ('res_f_fin', models.DateTimeField(blank=True, null=True)),
                ('res_precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio Reserva')),
            ],
            options={
                'verbose_name_plural': 'Reservas',
            },
        ),
        migrations.CreateModel(
            name='Vuelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vu_nombre', models.CharField(blank=True, max_length=50, null=True, verbose_name='Vuelo')),
                ('vu_origen', models.CharField(blank=True, max_length=50, null=True, verbose_name='Origen')),
                ('vu_destino', models.CharField(blank=True, max_length=50, null=True, verbose_name='Destino')),
                ('vu_precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio')),
                ('vu_asiento', models.CharField(max_length=20, verbose_name='Asiento')),
            ],
            options={
                'verbose_name_plural': 'Vuelos',
            },
        ),
    ]
