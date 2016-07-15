# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0037_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Email',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
