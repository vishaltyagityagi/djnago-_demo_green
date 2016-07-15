# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('green_state', '0008_auto_20160524_0819'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrationform',
            old_name='city',
            new_name='cityname',
        ),
    ]
