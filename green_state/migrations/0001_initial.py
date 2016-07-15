# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(unique=True, max_length=100)),
                ('city', models.TextField()),
                ('mobile', models.IntegerField(max_length=12)),
                ('pincode', models.IntegerField(max_length=12)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RegistrationForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=100)),
                ('firstname', models.CharField(unique=True, max_length=100)),
                ('lastname', models.CharField(unique=True, max_length=100)),
                ('email', models.EmailField(unique=True, max_length=100)),
                ('password', models.CharField(unique=True, max_length=100)),
                ('confirmpassword', models.CharField(unique=True, max_length=100)),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.FileField(upload_to=b'upload')),
                ('address', models.ForeignKey(to='green_state.Address')),
            ],
            options={
                'ordering': ('-post_date',),
            },
            bases=(models.Model,),
        ),
    ]
