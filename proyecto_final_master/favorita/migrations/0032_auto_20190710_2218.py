# Generated by Django 2.2.3 on 2019-07-10 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favorita', '0031_auto_20190710_0027'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Salary',
        ),
        migrations.AlterModelOptions(
            name='driverlicense',
            options={'verbose_name_plural': 'DriverLicenses'},
        ),
    ]
