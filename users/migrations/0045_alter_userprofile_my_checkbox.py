# Generated by Django 4.1.1 on 2024-05-06 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0044_alter_userprofile_my_checkbox'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='my_checkbox',
            field=models.BooleanField(default=False),
        ),
    ]