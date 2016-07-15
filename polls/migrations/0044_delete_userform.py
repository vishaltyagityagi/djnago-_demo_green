# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0043_userform_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserForm',
        ),
    ]
