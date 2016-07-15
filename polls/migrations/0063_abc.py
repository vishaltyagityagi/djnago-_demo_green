# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0062_cms'),
    ]

    operations = [
        migrations.CreateModel(
            name='abc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100)),
                ('content', models.CharField(default=b'', max_length=100)),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-post_date',),
                'db_table': 'aaaaaa',
            },
            bases=(models.Model,),
        ),
    ]
