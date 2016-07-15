# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0045_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='lastname',
            field=models.CharField(default=b'', unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
