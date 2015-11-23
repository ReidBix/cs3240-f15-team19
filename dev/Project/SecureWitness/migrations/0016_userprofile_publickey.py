# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0015_remove_userprofile_publickey'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(max_length=2000, default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCzzSPuT10L10q1mrVEfYuF4zp7\nu+loT/qd/gOph60V5Kf3TMqGFSIYNvvP65b++zX5D1PIYTK8pvMgzYebDCQ4nBop\naiORbsKbLng/L84dPvGVfamqyvifMlwr4hMBHfKEUKT+keCzcLAPj3TCKg7xZenX\nReI7Nktn0S77hk0bhQIDAQAB\n-----END PUBLIC KEY-----'),
        ),
    ]
