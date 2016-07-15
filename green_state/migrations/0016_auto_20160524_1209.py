# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('green_state', '0015_auto_20160524_1207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrationform',
            old_name='is_active',
            new_name='Is_Active',
        ),
    ]
