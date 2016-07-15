# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('green_state', '0003_registrationform_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrationform',
            name='image',
        ),
    ]
