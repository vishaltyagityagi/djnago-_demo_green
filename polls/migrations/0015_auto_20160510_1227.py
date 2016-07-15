# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_blog_object_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='object_id',
            field=models.PositiveIntegerField(db_index=True),
            preserve_default=True,
        ),
    ]
