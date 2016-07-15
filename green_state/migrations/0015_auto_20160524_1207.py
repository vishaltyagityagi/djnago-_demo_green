# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('green_state', '0014_registrationform_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrationform',
            old_name='confirmpassword',
            new_name='Confirm_Password',
        ),
        migrations.RenameField(
            model_name='registrationform',
            old_name='cityname',
            new_name='city_Name',
        ),
        migrations.RenameField(
            model_name='registrationform',
            old_name='firstname',
            new_name='first_Name',
        ),
        migrations.RenameField(
            model_name='registrationform',
            old_name='lastname',
            new_name='last_Name',
        ),
        migrations.RenameField(
            model_name='registrationform',
            old_name='username',
            new_name='user_Name',
        ),
    ]
