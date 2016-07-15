# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0042_auto_20160516_0546'),
    ]

    operations = [
        migrations.AddField(
            model_name='userform',
            name='image',
            field=models.FileField(default=b'', upload_to=b'userupload'),
            preserve_default=True,
        ),
    ]
