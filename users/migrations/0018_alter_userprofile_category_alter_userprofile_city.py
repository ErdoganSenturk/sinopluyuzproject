# Generated by Django 4.2.4 on 2024-02-09 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_alter_contact_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='category',
            field=models.CharField(choices=[('egitim', 'egitim'), ('saglik', 'saglik'), ('insaat', 'insaat '), ('gida', 'gida'), ('ulasimm', 'ulasim'), ('diger', 'diger')], default='sinoplu', max_length=20, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(choices=[('istanbul', 'istanbul'), ('sinop', 'sinop'), ('ankara', 'ankara')], default='sinope', max_length=20, verbose_name='Şehir'),
        ),
    ]