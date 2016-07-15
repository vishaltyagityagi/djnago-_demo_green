# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0020_auto_20160511_0710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='Image',
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default=b'', upload_to=b'images/%Y/%m/%d'),
            preserve_default=True,
        ),
    ]
