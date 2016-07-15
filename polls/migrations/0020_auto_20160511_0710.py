# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0019_auto_20160511_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Image',
            field=models.ImageField(default=b'', storage=django.core.files.storage.FileSystemStorage(location=b'/media/photos'), upload_to=b'Blog'),
            preserve_default=True,
        ),
    ]
