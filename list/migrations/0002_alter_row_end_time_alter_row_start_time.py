# Generated by Django 5.1 on 2024-09-01 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='row',
            name='end_time',
            field=models.TimeField(default='01:00', verbose_name='Godzina zakoczenia: '),
        ),
        migrations.AlterField(
            model_name='row',
            name='start_time',
            field=models.TimeField(default='00:00', verbose_name='Godzina rozpoczęcia: '),
        ),
    ]
