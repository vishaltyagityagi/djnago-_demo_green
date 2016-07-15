# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0036_auto_20160512_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('First_name', models.CharField(max_length=100)),
                ('Last_name', models.SlugField(max_length=100)),
                ('Email', models.TextField(unique=True)),
                ('Phone', models.CharField(unique=True, max_length=12)),
                ('image', models.FileField(upload_to=b'upload')),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
