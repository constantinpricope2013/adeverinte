# Generated by Django 3.0.5 on 2020-09-02 17:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adeverinte', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='date_posted',
        ),
        migrations.AddField(
            model_name='post',
            name='data_publish',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='post',
            name='time_publish',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
