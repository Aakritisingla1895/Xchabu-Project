# Generated by Django 2.1.3 on 2020-11-28 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='user',
        ),
    ]
