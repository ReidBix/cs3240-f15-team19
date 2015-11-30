# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0016_userprofile_publickey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCfGLbYxZC70PRtDNimf+HjwPk6\nE0BxtbsTrAOzCYiE4BC12A4YTO974l3jPcydzNA5Nv0l3uzDRf42dal+ip97hNYV\noin30Lxg5Od9iAvGQwevBURTwLzstdWafGvTHk526kUwXOvLX+xsR7/0YmyVHNs/\nrYURvKPxpNDsiFKYSwIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
    ]
