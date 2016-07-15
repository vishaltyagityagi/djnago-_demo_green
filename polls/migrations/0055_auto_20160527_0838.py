# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0054_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='email_from',
            field=models.EmailField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='email',
            name='to',
            field=models.EmailField(default=b'', max_length=100),
            preserve_default=True,
        ),
    ]
