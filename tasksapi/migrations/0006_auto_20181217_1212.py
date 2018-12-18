# Generated by Django 2.1.2 on 2018-12-17 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasksapi', '0005_auto_20181211_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskWhitelist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the whitelist.', max_length=50, unique=True)),
                ('description', models.TextField(blank=True, help_text='A description of the whitelist.')),
                ('user', models.ForeignKey(help_text='The maintainer of the whitelist.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('whitelisted_container_task_types', models.ManyToManyField(blank=True, help_text='The set of container task types to whitelist.', to='tasksapi.ContainerTaskType')),
                ('whitelisted_executable_task_types', models.ManyToManyField(blank=True, help_text='The set of executable task types to whitelist.', to='tasksapi.ExecutableTaskType')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='taskqueue',
            name='whitelists',
            field=models.ManyToManyField(blank=True, help_text='A set of task whitelists.', to='tasksapi.TaskWhitelist'),
        ),
    ]