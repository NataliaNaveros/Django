# Generated by Django 2.2.7 on 2019-11-27 01:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publicaciones', '0002_auto_20191126_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='post_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='publicacion',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
