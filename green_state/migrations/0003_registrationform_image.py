# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('green_state', '0002_remove_registrationform_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationform',
            name='image',
            field=models.FileField(default=b'', upload_to=b'upload'),
            preserve_default=True,
        ),
    ]
