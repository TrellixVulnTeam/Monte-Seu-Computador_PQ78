# Generated by Django 3.0.1 on 2019-12-18 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20191218_1908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cpu',
            name='name',
        ),
        migrations.RemoveField(
            model_name='cpu',
            name='quantity',
        ),
    ]
