# Generated by Django 2.2.7 on 2019-11-06 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seguidor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seguidor_id', models.IntegerField()),
                ('usuario_id', models.IntegerField()),
                ('validacion', models.BooleanField()),
            ],
        ),
    ]
