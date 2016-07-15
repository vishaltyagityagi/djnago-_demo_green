# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('green_state', '0004_remove_registrationform_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationform',
            name='city',
            field=models.TextField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='registrationform',
            name='mobile',
            field=models.IntegerField(default=b'', max_length=12),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='registrationform',
            name='pincode',
            field=models.IntegerField(default=b'', max_length=12),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='registrationform',
            name='state',
            field=models.CharField(default=b'', unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='address',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]
