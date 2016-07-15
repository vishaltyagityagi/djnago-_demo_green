# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_remove_blog_object_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='photo',
            new_name='Image',
        ),
    ]
