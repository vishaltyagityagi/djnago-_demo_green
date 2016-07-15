# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('green_state', '0023_registrationform_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(default=b'', max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('first_Name', models.CharField(max_length=100)),
                ('last_Name', models.CharField(max_length=100)),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('state', models.CharField(default=b'', max_length=100, choices=[(b'LAB', b'labor'), (b'CAR', b'cars'), (b'TRU', b'trucks'), (b'WRI', b'writing')])),
                ('city_Name', models.CharField(default=b'', max_length=100, choices=[(b'BRO', b'Bronx'), (b'BRK', b'Brooklyn'), (b'QNS', b'Queens'), (b'MAN', b'Manhattan'), (b'STN', b'Staten Island')])),
                ('address', models.CharField(default=b'', max_length=100)),
                ('phone', models.CharField(max_length=12)),
                ('pincode', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=100)),
                ('Confirm_Password', models.CharField(max_length=100)),
                ('Is_Active', models.BooleanField(default=b'')),
            ],
            options={
                'ordering': ('-post_date',),
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='RegistrationForm',
        ),
    ]
