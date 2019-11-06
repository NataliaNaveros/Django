# Generated by Django 2.2.7 on 2019-11-06 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario_id', models.IntegerField()),
                ('foto', models.ImageField(max_length=50, upload_to='')),
                ('descripcion', models.TextField()),
                ('crear', models.DateTimeField(auto_now_add=True)),
                ('actualizar', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]