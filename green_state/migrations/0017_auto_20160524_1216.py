# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('green_state', '0016_auto_20160524_1209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrationform',
            old_name='user_Name',
            new_name='username',
        ),
    ]
