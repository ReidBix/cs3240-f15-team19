# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0022_auto_20151119_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(max_length=2000, default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCoUyyVFreP/7OlcQ3oOWN8m5GE\nEyFUfj8kR9wnlyCU02QceakX1RXBoOfsLKrfpgHWFELfB72tTdxRDwJxdSQdXNXT\nuNMcU/+v/de0JUAZP3/TvH5CXekPNhte5w9ePsraVdgZbeHin8AjJ8Qbj2PB+QYF\n/jAesIO345+yC8PfywIDAQAB\n-----END PUBLIC KEY-----'),
        ),
    ]
