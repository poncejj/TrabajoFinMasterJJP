# Generated by Django 2.2 on 2019-07-04 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favorita', '0027_vehicletype_km_per_galon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='cast_time_rate',
            new_name='delivery_time_rate',
        ),
    ]