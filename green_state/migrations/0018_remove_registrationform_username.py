# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('green_state', '0017_auto_20160524_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrationform',
            name='username',
        ),
    ]
