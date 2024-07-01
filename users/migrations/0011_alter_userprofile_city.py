# Generated by Django 4.2.4 on 2024-01-22 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_userprofile_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(choices=[('İstanbul', 'istanbul'), ('Sinop', 'sinop'), ('Ankara', 'ankara')], default='sinope', max_length=20, verbose_name='Şehir'),
        ),
    ]