# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0040_auto_20160516_0537'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='AdminForm',
        ),
    ]
