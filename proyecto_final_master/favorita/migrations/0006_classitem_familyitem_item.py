# Generated by Django 2.2 on 2019-04-27 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('favorita', '0005_holidayevent_holidaylocale_holidaytype'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'ClassItems',
            },
        ),
        migrations.CreateModel(
            name='FamilyItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'FamiliyItems',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_nbr', models.IntegerField(default=0)),
                ('perishable', models.BooleanField()),
                ('class_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='favorita.ClassItem')),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='favorita.FamilyItem')),
            ],
            options={
                'verbose_name_plural': 'Items',
            },
        ),
    ]