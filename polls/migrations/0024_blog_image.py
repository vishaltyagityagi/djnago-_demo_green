# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0023_auto_20160511_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.FileField(default=b'', upload_to=b'documents/%Y/%m/%d'),
            preserve_default=True,
        ),
    ]
