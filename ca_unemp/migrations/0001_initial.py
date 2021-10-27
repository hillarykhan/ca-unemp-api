# Generated by Django 3.2.8 on 2021-10-27 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Unemployment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geoid', models.CharField(max_length=50)),
                ('county', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('labor_force', models.IntegerField()),
                ('value', models.PositiveIntegerField()),
                ('rate', models.FloatField()),
            ],
        ),
    ]