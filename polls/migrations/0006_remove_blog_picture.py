# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20160421_1104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='picture',
        ),
    ]
