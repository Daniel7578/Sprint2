# Generated by Django 3.2.6 on 2023-03-17 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('paciente', '0001_initial'),
        ('medico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('paciente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='paciente.paciente')),
                ('activa', models.BooleanField(default=True)),
                ('sintomas', models.TextField(max_length=500)),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('ultimaModificacion', models.DateTimeField(auto_now_add=True)),
                ('doctores', models.ManyToManyField(to='medico.medico')),
            ],
        ),
    ]
