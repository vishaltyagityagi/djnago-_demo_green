# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rent_service', models.TextField(default=b'', max_length=2000)),
                ('public_service', models.TextField(max_length=2000)),
                ('booking', models.TextField(max_length=2000)),
                ('renting', models.TextField(max_length=2000)),
                ('home_loan', models.TextField(default=b'', max_length=2000)),
                ('transport_service', models.TextField(default=b'', max_length=2000)),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-post_date',),
            },
            bases=(models.Model,),
        ),
    ]
