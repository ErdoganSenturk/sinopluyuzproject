# Generated by Django 4.1.1 on 2024-05-12 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0049_alter_userprofile_profile_pic1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='interests',
            field=models.CharField(blank=True, default='İnternet', max_length=255, null=True),
        ),
    ]
