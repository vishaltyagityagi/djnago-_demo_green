# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('green_state', '0009_auto_20160524_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationform',
            name='cityname',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
    ]
