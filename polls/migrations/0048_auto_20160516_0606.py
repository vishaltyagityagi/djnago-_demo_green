# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0047_product_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.FileField(default=b'', upload_to=b'upload'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=b''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='password',
            field=models.CharField(default=b'', unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='post_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='repassword',
            field=models.CharField(default=b'', unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
