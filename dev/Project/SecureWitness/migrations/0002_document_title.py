# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='title',
            field=models.CharField(default=datetime.datetime(2015, 11, 3, 17, 26, 17, 587835, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
