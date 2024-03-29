# Generated by Django 2.1.3 on 2019-08-28 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoContrato', models.CharField(choices=[('interno', 'Interno'), ('externo', 'Externo')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='FichaUsuario',
            fields=[
                ('rut', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('dv', models.CharField(max_length=1)),
                ('pNombre', models.CharField(max_length=30)),
                ('sNombre', models.CharField(max_length=30)),
                ('apPaterno', models.CharField(max_length=30)),
                ('apMaterno', models.CharField(max_length=30)),
                ('contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Contrato')),
            ],
        ),
    ]
