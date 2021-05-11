# Generated by Django 3.2 on 2021-05-11 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_auto_20210509_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accion', models.CharField(max_length=100)),
                ('tabla', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'registro',
            },
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_artist',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_suscribed',
            field=models.BooleanField(default=False),
        ),
    ]