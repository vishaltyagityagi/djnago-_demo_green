# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20160510_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='object_id',
            field=models.PositiveIntegerField(default=b''),
            preserve_default=True,
        ),
    ]
