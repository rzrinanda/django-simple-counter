# Generated by Django 4.1 on 2022-09-03 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='is_authenticated',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
