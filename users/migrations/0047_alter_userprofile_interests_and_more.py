# Generated by Django 4.1.1 on 2024-05-12 20:20

from django.db import migrations, models
import django_resized.forms
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0046_userprofile_interests_alter_userprofile_my_checkbox'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='interests',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic1',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], default='assets/img/default1.jpg', force_format='JPEG', keep_meta=True, null=True, quality=90, scale=0.9, size=[960, 600], upload_to=users.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic2',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], default='assets/img/default2.jpg', force_format='JPEG', keep_meta=True, null=True, quality=90, scale=0.9, size=[960, 600], upload_to=users.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic3',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], default='assets/img/default3.jpg', force_format='JPEG', keep_meta=True, null=True, quality=90, scale=0.9, size=[960, 600], upload_to=users.models.user_directory_path),
        ),
    ]
