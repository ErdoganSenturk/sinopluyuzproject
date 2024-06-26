# Generated by Django 4.2.4 on 2024-03-07 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import users.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0033_alter_userprofile_profile_pic1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic1',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', keep_meta=True, null=True, quality=90, scale=0.9, size=[960, 600], upload_to=users.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic2',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', keep_meta=True, null=True, quality=90, scale=0.9, size=[960, 600], upload_to=users.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic3',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', keep_meta=True, null=True, quality=90, scale=0.9, size=[960, 600], upload_to=users.models.user_directory_path),
        ),
        migrations.CreateModel(
            name='ProfileView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_view', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userprofile')),
            ],
        ),
    ]
