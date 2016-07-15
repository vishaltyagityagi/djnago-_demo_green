# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0026_blog_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='flag',
            field=models.BooleanField(default=b''),
            preserve_default=True,
        ),
    ]
