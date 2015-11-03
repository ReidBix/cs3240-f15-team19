# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0009_document_public'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='public',
            new_name='private',
        ),
    ]
