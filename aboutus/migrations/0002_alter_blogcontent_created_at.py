# Generated by Django 3.2.9 on 2022-04-08 18:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcontent',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 8, 18, 49, 5, 162947)),
        ),
    ]
