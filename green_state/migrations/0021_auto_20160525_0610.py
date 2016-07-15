# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('green_state', '0020_auto_20160525_0606'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrationform',
            old_name='User_Name',
            new_name='username',
        ),
    ]
