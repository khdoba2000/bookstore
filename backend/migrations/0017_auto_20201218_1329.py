# Generated by Django 3.1.4 on 2020-12-18 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_auto_20201218_0633'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='released_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='book',
            name='taken_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
