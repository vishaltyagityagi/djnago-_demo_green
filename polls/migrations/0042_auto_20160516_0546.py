# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0041_auto_20160516_0540'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(unique=True, max_length=100)),
                ('lastname', models.CharField(unique=True, max_length=100)),
                ('email', models.EmailField(unique=True, max_length=100)),
                ('phone', models.CharField(unique=True, max_length=100)),
                ('password', models.CharField(unique=True, max_length=100)),
                ('repassword', models.CharField(unique=True, max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='AdminForm',
        ),
    ]
