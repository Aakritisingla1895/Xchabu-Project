# Generated by Django 3.0.5 on 2020-07-25 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='East',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('layoutno', models.CharField(max_length=10)),
                ('bedl', models.DecimalField(decimal_places=1, max_digits=3)),
                ('bedw', models.DecimalField(decimal_places=1, max_digits=3)),
                ('bedx', models.CharField(max_length=3)),
                ('bedy', models.CharField(max_length=6)),
                ('kitl', models.DecimalField(decimal_places=1, max_digits=3)),
                ('kitw', models.DecimalField(decimal_places=1, max_digits=3)),
                ('kitx', models.CharField(max_length=3)),
                ('kity', models.CharField(max_length=20)),
                ('toil', models.DecimalField(decimal_places=1, max_digits=2)),
                ('toiw', models.DecimalField(decimal_places=1, max_digits=2)),
                ('toix', models.CharField(max_length=3)),
                ('toiy', models.CharField(max_length=6)),
                ('drawl', models.DecimalField(decimal_places=1, max_digits=3)),
                ('draww', models.DecimalField(decimal_places=1, max_digits=3)),
                ('drawx', models.CharField(max_length=3)),
                ('drawy', models.CharField(max_length=6)),
                ('stal', models.DecimalField(decimal_places=1, max_digits=3)),
                ('staw', models.DecimalField(decimal_places=1, max_digits=3)),
                ('stax', models.CharField(max_length=3)),
                ('stay', models.CharField(max_length=6)),
                ('dinl', models.CharField(max_length=1)),
                ('dinw', models.CharField(max_length=1)),
                ('dinx', models.CharField(max_length=1)),
                ('diny', models.CharField(max_length=1)),
                ('ctoil', models.CharField(max_length=3)),
                ('ctoiw', models.CharField(max_length=4)),
                ('ctoix', models.CharField(max_length=1)),
                ('ctoiy', models.CharField(max_length=20)),
                ('stol', models.CharField(max_length=3)),
                ('stow', models.CharField(max_length=4)),
                ('stox', models.CharField(max_length=7)),
                ('stoy', models.CharField(max_length=16)),
                ('otsl', models.DecimalField(decimal_places=1, max_digits=2)),
                ('otsw', models.DecimalField(decimal_places=1, max_digits=3)),
                ('otsx', models.CharField(max_length=3)),
                ('otsy', models.CharField(max_length=6)),
                ('washl', models.DecimalField(decimal_places=1, max_digits=2)),
                ('washw', models.DecimalField(decimal_places=1, max_digits=3)),
                ('washx', models.CharField(max_length=3)),
                ('washy', models.CharField(max_length=6)),
                ('entl', models.DecimalField(decimal_places=1, max_digits=2)),
                ('entw', models.DecimalField(decimal_places=1, max_digits=3)),
                ('entx', models.CharField(max_length=6)),
                ('enty', models.CharField(max_length=16)),
                ('parl', models.CharField(max_length=1)),
                ('parw', models.CharField(max_length=1)),
                ('parx', models.CharField(max_length=1)),
                ('pary', models.CharField(max_length=1)),
                ('garl', models.CharField(max_length=1)),
                ('garw', models.CharField(max_length=1)),
                ('garx', models.CharField(max_length=1)),
                ('gary', models.CharField(max_length=1)),
                ('foyl', models.CharField(max_length=1)),
                ('foyw', models.CharField(max_length=1)),
                ('foyx', models.CharField(max_length=1)),
                ('foyy', models.CharField(max_length=1)),
                ('util', models.DecimalField(decimal_places=1, max_digits=2)),
                ('utiw', models.DecimalField(decimal_places=1, max_digits=3)),
                ('utix', models.CharField(max_length=1)),
                ('utiy', models.CharField(max_length=1)),
            ],
        ),
    ]
