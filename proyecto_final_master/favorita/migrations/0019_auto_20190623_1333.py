# Generated by Django 2.2 on 2019-06-23 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorita', '0018_auto_20190623_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oil',
            name='dcoilwtico',
            field=models.FloatField(default=0),
        ),
    ]