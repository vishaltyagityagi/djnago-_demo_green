# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('green_state', '0021_auto_20160525_0610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrationform',
            name='username',
        ),
    ]
