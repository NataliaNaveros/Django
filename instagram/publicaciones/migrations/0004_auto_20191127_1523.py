# Generated by Django 2.2.7 on 2019-11-27 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0003_auto_20191126_2020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicacion',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='publicacion',
            name='slug',
        ),
    ]
