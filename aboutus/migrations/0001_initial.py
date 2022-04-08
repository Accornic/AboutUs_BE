# Generated by Django 3.2.9 on 2022-04-08 18:48

import datetime
from django.db import migrations, models
import mdeditor.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogContent',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('content', mdeditor.fields.MDTextField()),
                ('slug', models.SlugField(max_length=200)),
                ('created_by', models.CharField(max_length=200, unique=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 4, 8, 18, 47, 59, 63590))),
            ],
        ),
    ]
