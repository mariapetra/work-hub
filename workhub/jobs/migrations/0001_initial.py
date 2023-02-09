# Generated by Django 4.0.2 on 2023-02-09 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('location', models.TextField()),
                ('hours', models.IntegerField()),
                ('contract_type', models.TextField()),
                ('manager', models.CharField(max_length=200)),
                ('manager_email', models.EmailField(max_length=254)),
                ('salary', models.IntegerField()),
                ('notes', models.TextField()),
            ],
        ),
    ]
