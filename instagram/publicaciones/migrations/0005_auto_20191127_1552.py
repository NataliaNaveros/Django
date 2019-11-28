# Generated by Django 2.2.7 on 2019-11-27 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0003_auto_20191127_1552'),
        ('likes', '0002_auto_20191127_1552'),
        ('publicaciones', '0004_auto_20191127_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='publicaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='static/images/publicaciones')),
                ('mensaje', models.TextField(blank=True)),
                ('tipo', models.IntegerField(choices=[(1, 'Publicacion'), (2, 'Historia')], default=1)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Publicacion',
                'verbose_name_plural': 'Publicaciones',
            },
        ),
        migrations.DeleteModel(
            name='Publicacion',
        ),
    ]
