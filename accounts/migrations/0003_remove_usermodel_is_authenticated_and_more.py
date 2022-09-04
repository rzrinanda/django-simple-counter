# Generated by Django 4.1 on 2022-09-04 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_usermodel_is_authenticated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='is_authenticated',
        ),
        migrations.AddField(
            model_name='usermodel',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]