# Generated by Django 3.2 on 2021-05-27 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_auto_20210512_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=100)),
                ('enlace', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'articulos',
            },
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especie', models.CharField(max_length=100)),
                ('usuario', models.CharField(max_length=100)),
                ('lugar', models.CharField(max_length=100)),
                ('region', models.IntegerField(default=0)),
                ('link', models.URLField(default='https://www.google.com')),
                ('ubicacion', models.URLField(default='https://www.google.com/maps/?hl=es')),
            ],
            options={
                'db_table': 'Reportes',
            },
        ),
        migrations.RemoveField(
            model_name='historicalcustomuser',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalmusic',
            name='history_user',
        ),
        migrations.DeleteModel(
            name='Music',
        ),
        migrations.DeleteModel(
            name='PlaylistModel',
        ),
        migrations.DeleteModel(
            name='ReproduccionesModel',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='is_artist',
            new_name='is_expert',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_moderatorA',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_moderatorB',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_suscribed',
        ),
        migrations.DeleteModel(
            name='HistoricalCustomUser',
        ),
        migrations.DeleteModel(
            name='HistoricalMusic',
        ),
    ]
