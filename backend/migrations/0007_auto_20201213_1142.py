# Generated by Django 3.1.4 on 2020-12-13 11:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20201213_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='code',
            field=models.CharField(max_length=13, unique=True, validators=[django.core.validators.RegexValidator(message='Length has to be 13', regex='^.{13}$')]),
        ),
    ]