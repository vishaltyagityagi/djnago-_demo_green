# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0048_auto_20160516_0606'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-post_date',)},
        ),
        migrations.AlterField(
            model_name='product',
            name='email',
            field=models.EmailField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='firstname',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='lastname',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='password',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='repassword',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
    ]
