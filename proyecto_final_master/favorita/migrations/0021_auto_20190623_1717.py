# Generated by Django 2.2 on 2019-06-23 15:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorita', '0020_auto_20190623_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oil',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
