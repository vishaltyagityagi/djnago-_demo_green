# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('green_state', '0032_support'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
