# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0014_userprofile_publickey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='publickey',
        ),
    ]
