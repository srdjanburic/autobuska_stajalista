# Generated by Django 3.1.6 on 2021-02-08 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_linija'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='linija',
            name='uslov',
        ),
    ]
