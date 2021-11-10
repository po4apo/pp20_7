# Generated by Django 3.2.8 on 2021-10-24 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('post', models.CharField(max_length=200)),
                ('dateOfHiring', models.DateField()),
                ('departments', models.CharField(max_length=200)),
            ],
        ),
    ]
