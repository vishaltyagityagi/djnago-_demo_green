# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('green_state', '0024_auto_20160525_0639'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=12)),
                ('message', models.CharField(default=b'', max_length=100)),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-post_date',),
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='registration',
            name='pincode',
            field=models.CharField(max_length=6),
            preserve_default=True,
        ),
    ]
