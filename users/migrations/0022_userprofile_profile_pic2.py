# Generated by Django 4.2.4 on 2024-02-15 20:53

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_remove_userprofile_facebook_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic2',
            field=models.ImageField(blank=True, upload_to=users.models.user_directory_path),
        ),
    ]
