# Generated by Django 3.2.4 on 2021-07-07 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_contacto_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Componente',
            fields=[
                ('idComponente', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id')),
                ('nombreComponente', models.CharField(max_length=50, verbose_name='Componente')),
            ],
            options={
                'verbose_name': 'componente',
                'verbose_name_plural': 'componentes',
                'ordering': ['nombreComponente'],
            },
        ),
        migrations.AlterField(
            model_name='contacto',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AddField(
            model_name='producto',
            name='componente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.componente'),
            preserve_default=False,
        ),
    ]
