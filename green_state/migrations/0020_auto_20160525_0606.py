# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('green_state', '0019_registrationform_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrationform',
            old_name='user_Name',
            new_name='User_Name',
        ),
    ]
