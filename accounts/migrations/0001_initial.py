# Generated by Django 4.1 on 2022-09-03 08:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.TextField(validators=[django.core.validators.MinLengthValidator(8, 'the filed must contain at least 8 characters')])),
            ],
        ),
    ]
