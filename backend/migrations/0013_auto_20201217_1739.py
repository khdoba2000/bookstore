# Generated by Django 3.1.4 on 2020-12-17 17:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_book_is_taken'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=32, unique=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('passsword', models.CharField(max_length=32, unique=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('name', models.CharField(max_length=32, validators=[django.core.validators.MinLengthValidator(2)])),
                ('surname', models.CharField(max_length=32, validators=[django.core.validators.MinLengthValidator(2)])),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator])),
                ('phone_number', models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(message='Length has to be 9', regex='^.{9}$')])),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='taken_by',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='books', to='backend.user'),
            preserve_default=False,
        ),
    ]
