# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0012_auto_20151116_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='detailed_description',
            field=models.CharField(max_length=500, blank=True),
        ),
    ]
