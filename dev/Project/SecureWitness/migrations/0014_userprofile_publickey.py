# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0013_auto_20151116_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(blank=True, max_length=1024),
        ),
    ]
