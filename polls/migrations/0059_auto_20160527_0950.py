# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0058_auto_20160527_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('body', models.TextField()),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.FileField(upload_to=b'upload')),
                ('flag', models.BooleanField(default=b'')),
            ],
            options={
                'ordering': ('-post_date',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content_name', models.CharField(max_length=100)),
                ('page_url', models.CharField(default=b'', max_length=100)),
                ('content', models.TextField(default=b'')),
                ('header', models.TextField(default=b'')),
                ('footer', models.TextField(default=b'', max_length=100)),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-post_date',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email_from', models.EmailField(default=b'', max_length=100)),
                ('to', models.EmailField(default=b'', max_length=100)),
                ('subject', models.CharField(default=b'', max_length=100)),
                ('message', models.TextField(default=b'')),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-post_date',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(default=b'', max_length=100)),
                ('email', models.EmailField(default=b'', max_length=100)),
                ('is_active', models.BooleanField(default=b'')),
                ('password', models.CharField(default=b'', max_length=100)),
                ('repassword', models.CharField(default=b'', max_length=100)),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.FileField(default=b'', upload_to=b'upload')),
            ],
            options={
                'ordering': ('-post_date',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('servicetitle', models.CharField(max_length=100)),
                ('servicedescription', models.TextField(default=b'', max_length=100)),
                ('is_active', models.BooleanField(default=b'')),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.CharField(default=b'', max_length=3, choices=[(b'LAB', b'labor'), (b'CAR', b'cars'), (b'TRU', b'trucks'), (b'WRI', b'writing')])),
                ('user', models.CharField(default=b'', max_length=3, choices=[(b'BRO', b'Bronx'), (b'BRK', b'Brooklyn'), (b'QNS', b'Queens'), (b'MAN', b'Manhattan'), (b'STN', b'Staten Island')])),
                ('image', models.FileField(default=b'', upload_to=b'upload')),
            ],
            options={
                'ordering': ('-post_date',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='polls.Question'),
            preserve_default=True,
        ),
    ]
