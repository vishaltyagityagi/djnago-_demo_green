# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('green_state', '0011_auto_20160524_0834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrationform',
            name='username',
        ),
        migrations.AddField(
            model_name='registrationform',
            name='is_active',
            field=models.BooleanField(default=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='cityname',
            field=models.CharField(default=b'', max_length=100, choices=[(b'BRO', b'Bronx'), (b'BRK', b'Brooklyn'), (b'QNS', b'Queens'), (b'MAN', b'Manhattan'), (b'STN', b'Staten Island')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='mobile',
            field=models.CharField(max_length=12),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='pincode',
            field=models.CharField(max_length=12),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='state',
            field=models.CharField(default=b'', max_length=100, choices=[(b'LAB', b'labor'), (b'CAR', b'cars'), (b'TRU', b'trucks'), (b'WRI', b'writing')]),
            preserve_default=True,
        ),
    ]
