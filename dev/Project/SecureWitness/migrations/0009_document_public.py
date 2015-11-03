# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0008_document_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='public',
            field=models.BooleanField(default=datetime.datetime(2015, 11, 3, 23, 41, 39, 892744, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
