# Generated by Django 3.2 on 2021-05-27 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0010_alter_reports_region'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reports',
            name='usuario',
        ),
    ]
