# Generated by Django 4.1.6 on 2023-03-19 07:48

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
