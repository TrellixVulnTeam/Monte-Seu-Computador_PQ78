# Generated by Django 3.0.1 on 2019-12-18 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('restrictions', models.CharField(max_length=160)),
                ('quantity', models.IntegerField(max_length=1)),
            ],
        ),
    ]
