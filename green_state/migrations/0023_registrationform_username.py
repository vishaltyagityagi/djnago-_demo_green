# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('green_state', '0022_remove_registrationform_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationform',
            name='username',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
    ]
