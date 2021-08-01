# Generated by Django 2.1.7 on 2021-07-31 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rebmanagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pbs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pbs_code', models.CharField(blank=True, max_length=3, null=True)),
                ('pbs_name_en', models.CharField(blank=True, max_length=100, null=True)),
                ('pbs_name_bn', models.CharField(blank=True, max_length=150, null=True)),
                ('address_en', models.CharField(blank=True, max_length=200, null=True)),
                ('address_bn', models.CharField(blank=True, max_length=200, null=True)),
                ('lat_long_value', models.FloatField(blank=True, null=True)),
                ('office_head_name', models.CharField(blank=True, max_length=100, null=True)),
                ('office_head_Designation', models.CharField(blank=True, max_length=100, null=True)),
                ('office_head_mobile_num', models.CharField(blank=True, max_length=11, null=True)),
                ('complain_center_mobile_num', models.CharField(blank=True, max_length=11, null=True)),
                ('pbs_logo', models.ImageField(upload_to='pbs')),
                ('total_consumer_nos', models.IntegerField(blank=True, null=True)),
                ('total_billing_consumer_nos', models.IntegerField(blank=True, null=True)),
                ('total_service_area_km', models.IntegerField(blank=True, null=True)),
                ('total_line_km', models.IntegerField(blank=True, null=True)),
                ('total_employee_no', models.IntegerField(blank=True, null=True)),
                ('management', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rebmanagement.Management')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
    ]
