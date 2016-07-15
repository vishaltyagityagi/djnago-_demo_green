# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('green_state', '0006_auto_20160524_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationform',
            name='city',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
