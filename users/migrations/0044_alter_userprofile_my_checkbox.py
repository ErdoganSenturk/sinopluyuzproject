# Generated by Django 4.1.1 on 2024-05-06 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0043_remove_profileview_time_stamp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='my_checkbox',
            field=models.BooleanField(),
        ),
    ]
