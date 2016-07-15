# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20160421_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='photo',
        ),
        migrations.AddField(
            model_name='blog',
            name='picture',
            field=models.ImageField(default=b'', upload_to=b''),
            preserve_default=True,
        ),
    ]
