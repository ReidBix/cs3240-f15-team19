# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0042_auto_20151206_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(max_length=2000, default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCxrUKzORy/tyjG4TIMYSK21ZbX\nFtQBthvGETc0wVpXmaOM79gmObIAC0sBCUe70vIUXI5vQts4Bs1/83bdXS69hVXb\nQv602AuuoHUj/3/NTUgQmANSaw3ng8ejvuJTGnk7Sno/M8Tpqolzinh8MUiHlvtA\nWLUMLjml4waLBTfz/QIDAQAB\n-----END PUBLIC KEY-----'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(blank=True, max_length=2000, default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQCxrUKzORy/tyjG4TIMYSK21ZbXFtQBthvGETc0wVpXmaOM79gm\nObIAC0sBCUe70vIUXI5vQts4Bs1/83bdXS69hVXbQv602AuuoHUj/3/NTUgQmANS\naw3ng8ejvuJTGnk7Sno/M8Tpqolzinh8MUiHlvtAWLUMLjml4waLBTfz/QIDAQAB\nAoGAKy9ai+cwxqRFA/nOSVX+swO9EvBYfUX/AChFC8yHIc2VA/dzyO6zBfG4vDq+\nNbey4SIR+Jb+Y2K75gKN/IXeiwceNUnP8HCt+QLXU0hSBt8odpbMlf8aiYwASD4J\nMnBmGmPmtejnsPUCK672F7kIRemkVHw1TofV6wc2bN920h0CQQC3vFgXzuhA5cDh\nXs1WvE0OHTUWY/H07vFewEotk4BkEXh+gHgymxmGkHhmzUSJ7ESYzG3CMlBkrZu0\n0m+bDcU/AkEA947d29rj7p4hjBqH+ML/6hB9DQ3zY++KaPLnOyy2Tg/GG360zUqi\nBUpWxp6XJcLo+pQ7Bto+/cFqMDzAiH8LwwJASnwIGl6+uNBrSPHtvGPJuRcOFm2e\nAPV81DSP3boWKnsKpf3evGU0C+E1bjd4uZEWnfsB4+ARxz66CKvmoq0KcQJARceO\nf89GWldWa3B7DUKh8i8toIVjKrM1l3mIdiSXSo+lrtBbVFaKLuWSai//uNQk6aTo\nsnjIMqzXKrulJZRyEwJBAKWp4Tw4obBP9dpcruv5o/LG3P/5W/HP+jquqjFyldRP\njGnaDTeX+ibk5MsmuBd/CUNwZyVOGxeNFQl+dVAfPfg=\n-----END RSA PRIVATE KEY-----'),
        ),
    ]
