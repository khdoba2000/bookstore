# Generated by Django 3.1.4 on 2020-12-12 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('science', 'science'), ('religious', 'religious'), ('fiction', 'fiction'), ('biography', 'biography')], max_length=64),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]