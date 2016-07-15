# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('green_state', '0010_auto_20160524_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationform',
            name='confirmpassword',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='email',
            field=models.EmailField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='firstname',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='lastname',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='password',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='state',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='username',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
