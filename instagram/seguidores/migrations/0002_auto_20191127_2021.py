# Generated by Django 2.2.7 on 2019-11-28 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20191127_1552'),
        ('seguidores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='seguidores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seguidor', to='usuarios.usuarios')),
                ('usuario_seguido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seguido', to='usuarios.usuarios')),
            ],
            options={
                'verbose_name': 'Seguidor',
                'verbose_name_plural': 'Seguidores',
            },
        ),
        migrations.DeleteModel(
            name='Seguidor',
        ),
    ]
