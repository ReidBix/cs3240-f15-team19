# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0033_auto_20151130_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDtbpSac1dB+pleGnImxJGK1wwG\ntQCeQzOpsMcm03IQvrdf3Jof8OIqugGVuCkzxFPmk0YFeEOSIWoktC6JeTtTiUUp\nlNUbYgMqWsdF5Ijf63IneF1PraHXYz/ZL/2K0EvDlQ+TznbrAL7cT22B6MmDXcqH\n/NE6uVgSaj3ctOPT6QIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQDtbpSac1dB+pleGnImxJGK1wwGtQCeQzOpsMcm03IQvrdf3Jof\n8OIqugGVuCkzxFPmk0YFeEOSIWoktC6JeTtTiUUplNUbYgMqWsdF5Ijf63IneF1P\nraHXYz/ZL/2K0EvDlQ+TznbrAL7cT22B6MmDXcqH/NE6uVgSaj3ctOPT6QIDAQAB\nAoGAKOqrlUpXOTmUgJESJvgtFL4mhmle5+cw2gdq6pf5ykTzmQONU//RGgfgCgso\nnpEw3EV5BaxKCL7VaenbMzm/LTs0ivx2yInOODR33WVytokeH6+VgRSpqJUvcQTZ\nx8EcE4DdUqmGHw6ysK2KJNG2bKrfbn0vypxDtIncig7TAWECQQDwdXQTmbseR5xs\ns80mPHIE5ep7fMhM6dfzY2oELV3wiluxa7WsrAUiGnQPgJjqXfhMposQJTX6kRbf\nd2dl9u2lAkEA/McLwJGIar9z8Cjq6NG2B87QvL+Cv/5feuwGQxi9sgR8Z3O74sLF\nHr/7/MR22Lgxr0M8yStSCcCSg3O50nXB9QJAJIHQk8E9VYWNzDsoJGv86510kjcJ\nuhOuw7cOO4AfyQtYjIFL3eFoDhtyD4B4tux5bDnE1zivD1HD5T2dpy9sOQJBALSs\npNbIbuQ14e2HoZg1xNFB3ur6S79lVuOqbjNpLLVgBXeAPowvQOvgt4ENABGZXlHy\nUjFL2ICF93MjtW8boj0CQA3flMyS/qwDNtTbIwJpbseGpV1HnUHm4ygj23IYVvIL\nFNtdM1Ka0PfWcA0wTY7OYuMEwsE27mRAm2gIBYd8tHM=\n-----END RSA PRIVATE KEY-----', max_length=2000, blank=True),
        ),
    ]
