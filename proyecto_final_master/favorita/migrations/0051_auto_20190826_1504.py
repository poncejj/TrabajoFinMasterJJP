# Generated by Django 2.2.3 on 2019-08-26 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorita', '0050_auto_20190825_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metalog',
            name='best_fitness',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=18),
        ),
    ]