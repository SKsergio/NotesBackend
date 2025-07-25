# Generated by Django 5.1.5 on 2025-02-14 05:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Type of person',
                'verbose_name_plural': 'Types of people',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=100)),
                ('last_names', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('carnet', models.CharField(blank=True, max_length=12, null=True)),
                ('DUI', models.CharField(max_length=12, unique=True)),
                ('direction', models.TextField(max_length=500, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('photo', models.ImageField(max_length=300, upload_to='people_photos/')),
                ('institution_Role', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('type_Person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='people', to='MG_People.type')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'People',
                'ordering': ['created_at'],
            },
        ),
    ]
