# Generated by Django 2.2 on 2021-10-05 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='office_code',
            field=models.CharField(blank=True, db_index=True, max_length=3, unique=True),
        ),
    ]