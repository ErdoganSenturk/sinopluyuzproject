# Generated by Django 4.2.4 on 2024-02-15 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_userprofile_profile_pic2'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='facebook',
            field=models.URLField(blank=True, max_length=50),
        ),
    ]
