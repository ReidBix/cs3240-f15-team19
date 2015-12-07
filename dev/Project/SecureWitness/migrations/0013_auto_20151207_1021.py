# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0012_auto_20151207_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='folder',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDgWrK6UKV3yyHOk1oiOPEPRacB\nkhhrRqCFurq4uanyZCi6mcPf+w6RlSAaSaLXt0vVPbs4uLlcEPt72pd1Y+TOEPOv\ne/O1B/pAlJUYHK+t4BZeHEp7f9kqLnDy4iruJLABmW2VXRIhg0TdMKRVug5J2xse\n34JmOpk927PQV4ECWwIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(blank=True, default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQDgWrK6UKV3yyHOk1oiOPEPRacBkhhrRqCFurq4uanyZCi6mcPf\n+w6RlSAaSaLXt0vVPbs4uLlcEPt72pd1Y+TOEPOve/O1B/pAlJUYHK+t4BZeHEp7\nf9kqLnDy4iruJLABmW2VXRIhg0TdMKRVug5J2xse34JmOpk927PQV4ECWwIDAQAB\nAoGAA2VcDzXpS0bn3Bie5KW4AGMtg/iSJg2LoHqTGPi2edTKSQjKzjken1WChuNW\nc61ymGe2zcT+CUa4h8dnQ3+flveli7fPgVPk3utQ6WCxn4uHWUdXKOu+gUHtg/JQ\nleFmr3fHP8liA149GnIG4rFsexW8+A4cX/0OuB9QJ5tMYQECQQDguGWL4rQFebEh\n4nN8J8wZMUduRkU7bMqq9nQsh/Vpi5/Xt/m+rZlmtjDYZ6HqxmLdCK1pe5vI6FPo\nGvtFDBwfAkEA/5VCXKdrfMYHJEo0uphWH/RdNilOSsPbRdwTZgP0Ft32zFzyKlC5\nmE5/JlhjNrhJhEBumgtpCsx6+bgULlTSRQJAMbV4eP4X9lIZ9bXi9+bRxgzZkTIo\nJGIHXtQPlL4qckN5gz1mGGDMWyUYHvaloYpq2hwOSBQYvNNvpBs70+U+3wJBAJyO\nAShgJSc45gcErWffCGJqfO5APwTtE9OnCvriURHwxMxJ4syoxgbVjm0elyddmyq3\njQgvFRjYSDvO1g3LR0ECQQCV+gLBnowItijbByIjT1hUf7FEfyQdl2AEkh152kos\nVcRJOAk5YuHBI6gws7ELc1OSl1HOXpXsDBAYYnmlEEX0\n-----END RSA PRIVATE KEY-----', max_length=2000),
        ),
    ]
