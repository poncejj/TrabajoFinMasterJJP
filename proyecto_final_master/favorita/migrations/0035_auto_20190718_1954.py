# Generated by Django 2.2.3 on 2019-07-18 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favorita', '0034_auto_20190713_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='configuration',
            old_name='night_hour_rate',
            new_name='weekend_hour_rate',
        ),
    ]
