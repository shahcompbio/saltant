# Generated by Django 2.1.2 on 2018-12-05 06:27

from django.db import migrations
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tasksapi', '0003_auto_20181204_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='time_zone',
            field=timezone_field.fields.TimeZoneField(default='America/Vancouver'),
        ),
    ]
