# Generated by Django 2.2 on 2019-06-28 17:37

from django.db import migrations, models
import django.utils.timezone
import favorita.forms


class Migration(migrations.Migration):

    dependencies = [
        ('favorita', '0022_results'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('algorithm', models.CharField(choices=[('GA', 'Genetic Algorithm'), ('TS', 'Tabu Search'), ('AC', 'Ant Colony Optimization')], default='GA', max_length=2)),
                ('selected', models.BooleanField(blank=True, null=True)),
                ('route_date', models.DateField(default=django.utils.timezone.now)),
                ('parameter1', models.FloatField(blank=True, default=0, null=True)),
                ('parameter2', models.FloatField(blank=True, default=0, null=True)),
                ('parameter3', models.FloatField(blank=True, default=0, null=True)),
                ('parameter4', models.FloatField(blank=True, default=0, null=True)),
                ('parameter5', models.FloatField(blank=True, default=0, null=True)),
                ('parameter6', models.FloatField(blank=True, default=0, null=True)),
                ('distance_rate', favorita.forms.MinMaxFloat(default=0)),
                ('num_trucks_rate', favorita.forms.MinMaxFloat(default=0)),
                ('staff_cost_rate', favorita.forms.MinMaxFloat(default=0)),
                ('gasoline_cost_rate', favorita.forms.MinMaxFloat(default=0)),
                ('cast_time_rate', favorita.forms.MinMaxFloat(default=0)),
                ('total_time', models.IntegerField(blank=True, default=0, null=True)),
                ('distance_result', models.FloatField(blank=True, default=0, null=True)),
                ('num_trucks_result', models.FloatField(blank=True, default=0, null=True)),
                ('staff_cost_result', models.FloatField(blank=True, default=0, null=True)),
                ('gasoline_cost_result', models.FloatField(blank=True, default=0, null=True)),
                ('cast_time_result', models.FloatField(blank=True, default=0, null=True)),
                ('errors', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Results',
        ),
        migrations.AlterField(
            model_name='holidayevent',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='oil',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='sale',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]