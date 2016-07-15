# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_auto_20160511_0847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
        migrations.AddField(
            model_name='blog',
            name='docfile',
            field=models.FileField(default=b'', upload_to=b'documents/%Y/%m/%d'),
            preserve_default=True,
        ),
    ]
