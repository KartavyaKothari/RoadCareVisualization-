# Generated by Django 3.0.7 on 2020-06-23 07:45

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoadData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('multipoint', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
                ('osm_id', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='RoadPothole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('rating', models.FloatField()),
                ('bearing', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='RoadPothole_snapped',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('rating', models.FloatField()),
                ('bearing', models.FloatField()),
                ('total_potholes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RoadPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('bearing', models.FloatField()),
                ('sequence_number', models.IntegerField()),
                ('roaddata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RoadMapView.RoadData')),
            ],
        ),
    ]
