# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('green_state', '0036_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='address',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='registration',
            name='city_Name',
            field=models.CharField(max_length=100, choices=[(b'BRO', b'Bronx'), (b'BRK', b'Brooklyn'), (b'QNS', b'Queens'), (b'MAN', b'Manhattan'), (b'STN', b'Staten Island')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='registration',
            name='state',
            field=models.CharField(max_length=100, choices=[(b'LAB', b'labor'), (b'CAR', b'cars'), (b'TRU', b'trucks'), (b'WRI', b'writing')]),
            preserve_default=True,
        ),
    ]
