# Generated by Django 4.2.4 on 2023-11-29 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_userprofile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]