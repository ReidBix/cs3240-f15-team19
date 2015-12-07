# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0010_auto_20151207_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='folder',
            field=models.CharField(max_length=2000, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(max_length=2000, default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDCdaHe9FcUVZ+UhiW+MPNQwGlk\nc/s9cPetLHF4hPpABR5wVk6d8vIOCeUkLuZT57FG4Y5kjr9y/d6u6xqxNxjgYRlg\njMs5fr3r/vNSfX9XNLpdvKMBOVeG9CAOkmw3ykGlb/U6wB2Ft6u1uXwloydfAmSj\nZfTI64JGhbMgLesdhQIDAQAB\n-----END PUBLIC KEY-----'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(max_length=2000, blank=True, default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQDCdaHe9FcUVZ+UhiW+MPNQwGlkc/s9cPetLHF4hPpABR5wVk6d\n8vIOCeUkLuZT57FG4Y5kjr9y/d6u6xqxNxjgYRlgjMs5fr3r/vNSfX9XNLpdvKMB\nOVeG9CAOkmw3ykGlb/U6wB2Ft6u1uXwloydfAmSjZfTI64JGhbMgLesdhQIDAQAB\nAoGBALn6tRi+CXZ6OYhcEEbpHBw0GdgoELZ/j3GBWvjP/WMzQhxgfwoTK6t/jTZg\n4IqIwgSvfnbwC2xYHxyd4EZzEocCmcMsFrYN3RuDbysjZou3s92lDb2Jqyavg4XB\nL1QmG34Sk8IQU5nZitgAuJkK9YoKbukxcmXqiRDc5Ok+68sBAkEAz8u6l07Z0xM9\nfwGlNhww03kZ2iIfyiJzBOxq6NnmZUXQtwllg4hi97HGsKlcSeMfg9S/3PcAgtRP\n3Xbfsz6HQQJBAO+R5/Qli4FKmuSWLpwstKfTQdSpAJuz97BPjvoB6Xe1Jr9CwKGJ\nH4KuKu2vULh7R6i1S1xX6eu+sPE/TWHXaUUCQDvsITPO/ku7Kam9fLoc6QuiyYy4\n+Hfe9VI/Jxlc9O7Rcj3GTOrgYsHRF14MiNuZzpXCvU1oQVJ5DUrtI9dZucECQHsW\ndB60y6B6PGsF3pzPO2Ke4EvrKSzWooQr3EIHiXS/1lCec2qLkW0LH3NPiCHA9Whw\n/W9MnBtLto29AH0suCECQQDDUBcqRsSQN2xtBRWHiyIeUw+cJE4b1dK+kNSpjH8O\nsJ4h0L8n9YeRWtqTsVyWIK8cAMrOhZF1JSafSPN0iwsS\n-----END RSA PRIVATE KEY-----'),
        ),
    ]
