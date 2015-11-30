# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0019_auto_20151119_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(max_length=2000, default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDGWAUGUCSkSiXF7ijkyaN0NqxQ\ncnSaIWgK6gb6Stae6zklldREFUfiwfNeT3C0rWPJCfC9feaEvJ3cc32N5UNy8kVk\n9S5/BR+XFNf15O6dtg4Hc7nSrcDdMUSv56HAvgVCmoDCECMvxd1prHARrlsEAw/3\n8qI2i9bfZxnIrtwmwQIDAQAB\n-----END PUBLIC KEY-----'),
        ),
    ]
