# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0051_auto_20160523_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='servicedescription',
            field=models.TextField(default=b'', max_length=100),
            preserve_default=True,
        ),
    ]
