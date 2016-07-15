# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('green_state', '0025_auto_20160525_0921'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact_us',
            new_name='Contact',
        ),
    ]
