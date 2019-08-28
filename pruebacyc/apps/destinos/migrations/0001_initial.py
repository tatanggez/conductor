# Generated by Django 2.1.3 on 2019-08-28 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comuna', models.CharField(choices=[('Peñalolen', 'Peñalolen'), ('La Reina', 'La Reina'), ('Vitacura', 'Vitacura'), ('Las Condes', 'Las Condes'), ('Lo Barnechea', 'Lo Barnechea'), ('La Dehesa', 'La Dehesa'), ('Estación Central', 'Estación Central'), ('Quinta Normal', 'Quinta Normal'), ('Pedro Aguirre Cerda', 'Pedro Aguirre Cerda'), ('Lo Prado', 'Lo Prado'), ('Pudahuel', 'Pudahuel'), ('Cerro Navia', 'Cerro Navia'), ('Lo Espejo', 'Lo Espejo'), ('Cerrillos', 'Cerrillos'), ('Maipú', 'Maipú')], max_length=50)),
                ('Direccion', models.CharField(max_length=5)),
            ],
        ),
    ]
