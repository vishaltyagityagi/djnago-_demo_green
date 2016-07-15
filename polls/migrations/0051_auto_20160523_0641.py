# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0050_service'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='users',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='service',
            name='email',
        ),
    ]
