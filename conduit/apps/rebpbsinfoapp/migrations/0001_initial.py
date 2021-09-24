# Generated by Django 2.2 on 2021-09-19 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NetMeterInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('install_meter_nos', models.IntegerField(blank=True, null=True)),
                ('capacity_of_install_meter', models.IntegerField(blank=True, null=True)),
                ('month', models.CharField(blank=True, max_length=50, null=True)),
                ('year', models.CharField(blank=True, max_length=50, null=True)),
                ('fy', models.CharField(blank=True, max_length=50, null=True)),
                ('pbs_code', models.CharField(blank=True, max_length=3, null=True)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
    ]