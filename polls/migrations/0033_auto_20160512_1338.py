# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0032_auto_20160512_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.FileField(upload_to=b'/upload/%Y/%m/%d'),
            preserve_default=True,
        ),
    ]
