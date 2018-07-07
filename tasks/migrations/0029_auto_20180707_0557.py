# Generated by Django 2.0.6 on 2018-07-07 05:57

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0028_auto_20180707_0557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasktype',
            name='required_arguments_default_values',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='A JSON dictionary of default values for required arguments, where the keys are the argument names and the values are their corresponding default values'),
        ),
    ]