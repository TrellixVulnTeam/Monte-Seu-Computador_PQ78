# Generated by Django 3.0.1 on 2019-12-18 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_cpu_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpu',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
