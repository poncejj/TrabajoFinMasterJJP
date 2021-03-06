# Generated by Django 2.2 on 2019-04-27 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('favorita', '0003_auto_20190427_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'States',
            },
        ),
        migrations.CreateModel(
            name='StoreType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter', models.CharField(max_length=1)),
            ],
            options={
                'verbose_name_plural': 'StoreTypes',
            },
        ),
        migrations.RemoveField(
            model_name='store',
            name='state',
        ),
        migrations.AlterField(
            model_name='store',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='favorita.City'),
        ),
        migrations.AlterField(
            model_name='store',
            name='store_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='favorita.StoreType'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='favorita.State'),
        ),
    ]
