# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0037_auto_20151130_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(max_length=2000, default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDEmlx4y8QwA9YtGOMmeTHh7P+p\neI07tkIoXqR8Oa8WyiSFvQgNCCiPbN6je26kZPLtlo9tB0cZaEr1vv4nECP7fpKz\nFdvhOY9S0UyQxnPbrlqqehXXDIkM2stUI6cbwrK9yJbXu+sMGoIMaHUCLS6lHxFD\nIQKw/orR+owAP086CwIDAQAB\n-----END PUBLIC KEY-----'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(max_length=2000, default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQDEmlx4y8QwA9YtGOMmeTHh7P+peI07tkIoXqR8Oa8WyiSFvQgN\nCCiPbN6je26kZPLtlo9tB0cZaEr1vv4nECP7fpKzFdvhOY9S0UyQxnPbrlqqehXX\nDIkM2stUI6cbwrK9yJbXu+sMGoIMaHUCLS6lHxFDIQKw/orR+owAP086CwIDAQAB\nAoGATtlJtPikGk2vnC6bC1cX9nBCqQk8O3KBXgd3GItZ+V3g//IsRG29NqiHMjHS\n0gPamgcERsngbgQx7BVJgQksJIDLzwYaUtn7QIx0TojR4jfluYdTgbRcKTy3Bw1L\nLlRxvO0P7IMZF7FboAb3sV2c2NZLAQDy+6bINQfa1dyLuOECQQDQBc9bgunsE52H\nA7v6pdw56bOXojUMln0aOc6Vt4Gia4KQGvqg+xcx3+86igCjo74oovkGFbMhaUiW\n7kqIKOnHAkEA8fJNP9jb/Uj1dWdijqKHZ5XYQKUF2mlo+rtTuQC/ad8KnIW+dDdD\ndxz6NTTAlG34gKi8I4ksNTgEk7tXSOFNnQJBAJRHf+4wHAQeW0xROh5JOfjCADUW\n9494ecZG7F3GB4656cBEquAy+u6fPAxTMG90mWin+q/+qcgoHwkO5Gu4FiMCQHFu\nznTusUUw3ZProrOI077m6/py5CmgXg2fogMMrLFwVsNHmSFXf5PqzAwB7YAphuab\nNYnbmBRjbRHuNV//8akCQQCIj07HvBJsgqOB8kzDGyb2v22Ooxx1qeqwg1am0Sq0\nFNwJzmYOefa8/EiUaN3TIsTDGn8Da3jNHMqhL/a4zVTz\n-----END RSA PRIVATE KEY-----', blank=True),
        ),
    ]
