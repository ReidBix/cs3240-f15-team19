# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0024_auto_20151119_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICWwIBAAKBgQDfQBmVhN4pY9++zr2pn/jLYSbcEHniu5qFVFyNKJ1iMVv2s5lF\nKEs7QhFL0pztiWutgd1K4H03z6af93HBT5ud2R/q58GML2OBuV7EsoRFKpbo+Pgg\nIpCSNfFEM/rfSRiT4YIOty/OqrDJrh8Ru/InDoA4Bn5cfvgrBg0CFA1KOwIDAQAB\nAoGAEOEMziQ0k9aMRSXmaxvAOMhIotzQCld60FfXg4itlY370QQ1M2hff8R4AE6V\nNNRuArlN3OpqLT0S8QdJX39AWaOr8bLCjdeObSpVtB78eamXjfmtjut1pidWDAys\n6IDwJYd4qHXsc8gkXwown8ZXW8TzXTH08OMc/dkRpegfS6ECQQDiexQBlxF2Jx03\nEpOtz7sg5idCBwx29MvFBL+2WFdm2BpPTkqqln2bAU/n6H0f13AJ/tGh4b+okJi3\nqXhexeSrAkEA/Fk8BdLTEKOiNZT2wZz/hUMK6XFHSGHg8i3nziGQ1Gx4JOvMzV2O\nM7AjT0w63pceVOOoxBTllDpd3PVjsc6QsQJAZaQe4mfN6ly7e8/WfxbPQICJ9dP8\nABb0rELpVwhmkT1C8XyNfel0DXCVT9rC7Nte6N13b1NFFH1wTFy+LKpbaQJAaeZM\n4SjDeLUjCpd0InZvaQ5kkuj+ACtLSnbnU8MUU4EdvmjSbtC3L4vYlZupDOagTQGp\nPniCi/0ejO7SIrlMUQJAaawaUUqnGT8dE/1Gxrhp5b9UaVIrb+u/LtXEDPry/6C+\nTfOTav8FYw0KPhcOlBzQBDcp+6jmUf1qjdW5mWoPaQ==\n-----END RSA PRIVATE KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDfQBmVhN4pY9++zr2pn/jLYSbc\nEHniu5qFVFyNKJ1iMVv2s5lFKEs7QhFL0pztiWutgd1K4H03z6af93HBT5ud2R/q\n58GML2OBuV7EsoRFKpbo+PggIpCSNfFEM/rfSRiT4YIOty/OqrDJrh8Ru/InDoA4\nBn5cfvgrBg0CFA1KOwIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
    ]
