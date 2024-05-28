# Generated by Django 5.0.6 on 2024-05-28 10:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0002_alter_encuesta_name_alter_encuesta_subtitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(max_length=10, verbose_name='Orden')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('subtitle', models.CharField(max_length=200, verbose_name='Subtítulo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de última modificación')),
                ('encuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuestas.encuesta', verbose_name='Encuesta')),
            ],
            options={
                'verbose_name': 'sección',
                'verbose_name_plural': 'secciones',
                'ordering': ['-created'],
            },
        ),
    ]
