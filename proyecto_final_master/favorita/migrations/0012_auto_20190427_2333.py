# Generated by Django 2.2 on 2019-04-27 21:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('favorita', '0011_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_nbr',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('unit_sales', models.IntegerField(default=0)),
                ('onpromotion', models.BooleanField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='favorita.Item', to_field='item_nbr')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='favorita.Store')),
            ],
            options={
                'verbose_name_plural': 'Sales',
            },
        ),
    ]
