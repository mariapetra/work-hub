# Generated by Django 4.1.6 on 2023-02-06 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_alter_jobs_end_date_alter_jobs_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='start_date',
        ),
    ]
