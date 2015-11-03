# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0004_document_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='description',
            field=models.CharField(max_length=100, default=datetime.datetime(2015, 11, 3, 19, 14, 56, 778870, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='detailed_description',
            field=models.CharField(max_length=500, default=datetime.datetime(2015, 11, 3, 19, 15, 0, 637703, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='encrypted',
            field=models.BooleanField(default=datetime.datetime(2015, 11, 3, 19, 15, 4, 693764, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
