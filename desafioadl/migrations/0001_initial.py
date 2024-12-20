# Generated by Django 5.1.3 on 2024-11-19 21:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=255)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubTarea',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=255)),
                ('estado', models.BooleanField(default=True)),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtareas', to='desafioadl.tarea')),
            ],
        ),
    ]
