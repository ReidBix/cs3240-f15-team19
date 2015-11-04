# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0010_auto_20151103_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='user',
            field=models.CharField(max_length=25, default=datetime.datetime(2015, 11, 4, 0, 39, 58, 778407, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
