# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0025_auto_20160511_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='flag',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
