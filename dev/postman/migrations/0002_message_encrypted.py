# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postman', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='encrypted',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
