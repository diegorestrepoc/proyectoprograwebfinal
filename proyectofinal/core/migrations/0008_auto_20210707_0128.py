# Generated by Django 2.2.3 on 2021-07-07 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_usuario_fechanacimiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('placa_madre', models.IntegerField(choices=[[0, 'MSI H310M PRO-VDH PLUS'], [1, 'ASUS PRIME B460M-A'], [2, 'MSI A320M-A PRO MAX']])),
                ('procesador', models.IntegerField(choices=[[0, 'I5-10400F'], [1, 'RYZEN 3 3200G'], [2, 'I3-9100']])),
                ('gpu', models.IntegerField(choices=[[0, 'GTX 1650 TI'], [1, 'GTX 3060'], [2, 'RX 580']])),
                ('ram', models.IntegerField(choices=[[0, 'CRUCIAL 4GB'], [1, 'HYPERX 4GB'], [2, 'A-DATA 8GB']])),
                ('fuente', models.IntegerField(choices=[[0, 'GIGABYTE 550W'], [1, 'CORSAIR 450W'], [2, 'GAMEMAX 650W']])),
                ('discoduro', models.IntegerField(choices=[[0, 'WD 500GB'], [1, 'SEAGATE 2TB'], [2, 'WD 4TB']])),
                ('gabinete', models.IntegerField(choices=[[0, 'GEAR BLACKSTAR'], [1, 'DINON MODEL'], [2, 'POWER TRAIN LASER FIVE G1']])),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
            ],
            options={
                'verbose_name': 'Cotización',
                'verbose_name_plural': 'Cotizaciones',
                'ordering': ['-created'],
            },
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'ordering': ['usuario'], 'verbose_name': 'usuario', 'verbose_name_plural': 'usuarios'},
        ),
    ]
