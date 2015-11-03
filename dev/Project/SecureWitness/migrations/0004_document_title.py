# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0003_remove_document_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='title',
            field=models.CharField(default=datetime.datetime(2015, 11, 3, 18, 11, 6, 384345, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
