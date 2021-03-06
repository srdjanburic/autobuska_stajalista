# Generated by Django 3.1.6 on 2021-02-08 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210207_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Linija',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=200)),
                ('broj_stanica', models.IntegerField(default=0)),
                ('uslov', models.BooleanField(default=False)),
                ('stanice', models.ManyToManyField(to='app.Stanica')),
            ],
        ),
    ]
