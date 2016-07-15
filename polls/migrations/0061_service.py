# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0060_auto_20160527_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('servicetitle', models.CharField(max_length=100)),
                ('servicedescription', models.TextField(default=b'', max_length=100)),
                ('is_active', models.BooleanField(default=b'')),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.CharField(default=b'', max_length=3, choices=[(b'LAB', b'labor'), (b'CAR', b'cars'), (b'TRU', b'trucks'), (b'WRI', b'writing')])),
                ('user', models.CharField(default=b'', max_length=3, choices=[(b'BRO', b'Bronx'), (b'BRK', b'Brooklyn'), (b'QNS', b'Queens'), (b'MAN', b'Manhattan'), (b'STN', b'Staten Island')])),
                ('image', models.FileField(default=b'', upload_to=b'upload')),
            ],
            options={
                'ordering': ('-post_date',),
            },
            bases=(models.Model,),
        ),
    ]
