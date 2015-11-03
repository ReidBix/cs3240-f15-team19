# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0006_document_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='created',
        ),
    ]
