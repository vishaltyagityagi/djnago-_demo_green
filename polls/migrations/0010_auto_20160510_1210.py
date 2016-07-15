# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_blog_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=100)),
                ('email', models.EmailField(unique=True, max_length=100)),
                ('password1', models.CharField(unique=True, max_length=100)),
                ('password2', models.CharField(unique=True, max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='blog',
            name='object_id',
            field=models.PositiveIntegerField(default=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
