# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_remove_blog_object_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='object_id',
            field=models.PositiveIntegerField(default=b''),
            preserve_default=True,
        ),
    ]
