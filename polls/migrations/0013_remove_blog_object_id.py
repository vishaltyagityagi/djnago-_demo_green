# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20160510_1220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='object_id',
        ),
    ]
