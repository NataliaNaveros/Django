# Generated by Django 2.2.7 on 2019-11-27 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20191127_1552'),
        ('publicaciones', '0005_auto_20191127_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicaciones',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuarios'),
        ),
    ]