# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0002_auto_20151207_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDrCOclEYq2hOvWnGGhim+G5t7t\n8zzvg0tMkqLTviw8hZ101L+sMoxSsDd3hc3nIRv/cp5+Zczqx+fw7n/ZcYF6BYC0\nnA/Mz8XQuS3bb0IhDd0LPjZLaC+drNe2KhGdvKqxw4KpVrQDEMRnHuu7TAGG7dsQ\n/9j5XYUAMfAhnGTWKwIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXgIBAAKBgQDrCOclEYq2hOvWnGGhim+G5t7t8zzvg0tMkqLTviw8hZ101L+s\nMoxSsDd3hc3nIRv/cp5+Zczqx+fw7n/ZcYF6BYC0nA/Mz8XQuS3bb0IhDd0LPjZL\naC+drNe2KhGdvKqxw4KpVrQDEMRnHuu7TAGG7dsQ/9j5XYUAMfAhnGTWKwIDAQAB\nAoGBALxNQ7LlHPciAzjLzUR4/uVbrpuBVv6ld/x/NsjiAdrzSbVChdXWIapV1/qA\nTviwBBhioiyuLsCjLGZRDkkNsSaiXG10vXzMpK+hZwGNG1sQlMBzjDco+Vjl8HkI\ngcJ3XAuW5GP0ZwmcIHT1ty0CwR8v8JYXG9qdm/WRLYoaIzKBAkEA7N9jQQOrtsW7\nuZsr5JzYXWIYi6MprMMiG9r7GtAXga+zyLW8A2PB7j5BBS3gezGHht7A3rnmMFny\nT2Sscg3nSwJBAP4DhhC39+XeAADgZg40jveRYXNzl7x0dbgVR5cO155m4CBhySd1\nC8AxIcomr+QUkaCJ5rg8rlxXjaP3KfcXIKECQE3/UON7nfNVMPdxDQb+TpCRWJvC\nYlqs9nJNrRmrI9JkVMLmdL54/sbAYRCfhqeKK6JRfxjYBeAt/gf+knoL8fkCQQCb\nV25SpR8ubYCVCKaBA3V3Q2pUX5mo/5PKWwEoCUSls4ZXZ1XMEpF4HNPsO5KPqmCQ\nzCTUARAkmsqdPpdka7lhAkEAwXByN4KL7+IY8EFCfebe4NBQBuX27KplQaltJLjz\nOe2boacD5R/yNGPn34gF3MLJuRMMSP4I5nw78tDygv26TQ==\n-----END RSA PRIVATE KEY-----', max_length=2000, blank=True),
        ),
    ]
