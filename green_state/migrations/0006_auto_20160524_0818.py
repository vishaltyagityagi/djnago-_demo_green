# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('green_state', '0005_auto_20160524_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationform',
            name='mobile',
            field=models.IntegerField(max_length=12),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='pincode',
            field=models.IntegerField(max_length=12),
            preserve_default=True,
        ),
    ]
