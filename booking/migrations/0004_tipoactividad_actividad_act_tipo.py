# Generated by Django 4.0.4 on 2023-11-13 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_pack_pa_precio_reserva_actividad_reserva_hotel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoActividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tact_nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('tact_imagen', models.ImageField(default='', upload_to='TipoActividad/')),
            ],
            options={
                'verbose_name_plural': 'Tipo de Actividades',
            },
        ),
        migrations.AddField(
            model_name='actividad',
            name='act_tipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.tipoactividad'),
        ),
    ]
