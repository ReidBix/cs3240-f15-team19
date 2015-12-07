# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0011_auto_20151207_1005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='folder',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(max_length=2000, default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDdz/jhoV9YYU81GiI0WX2b9REs\nu7S/L8zKupSEuOx/hiEdHXeQor6x14dswq9mBijuvvlE4Dfuv5Yn9uF8XUEt7FhL\nU8bYIv33EKcHCeDg+wLOf2KqDBfB8L4/BlH2SQZtrNfwQonkdlHy5ho/4TxTOA3Y\nIi01HkEb24Xz7450ZQIDAQAB\n-----END PUBLIC KEY-----'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(max_length=2000, blank=True, default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQDdz/jhoV9YYU81GiI0WX2b9REsu7S/L8zKupSEuOx/hiEdHXeQ\nor6x14dswq9mBijuvvlE4Dfuv5Yn9uF8XUEt7FhLU8bYIv33EKcHCeDg+wLOf2Kq\nDBfB8L4/BlH2SQZtrNfwQonkdlHy5ho/4TxTOA3YIi01HkEb24Xz7450ZQIDAQAB\nAoGAej1D5mx9VAKEmTomwXzUCV+8ME/do0NfdBXxBVe4FetAUoBLxSy7NN0XZ+u+\np9YbNr+ONdPvXya8RJf82gG2ieYfws8+0QC5c60ib0X/FMzfu9wc1fb+PDNfOgZn\n8zm33wE4TOTkWfu9JXH80xQw2K6LxRjotdei1v81VjP46t0CQQDeWHKLJ/DO/KBL\nFRp0NOG565wBfp0JLksdSiLUXqm6kBZt6crSwtDtskPh4GNtD8OSK37poh4/wUnm\nN2ciIVojAkEA/2LeIMca/UIV7tfUuR+365G3bC/dRG7GejuhKbUGnRzVpZWt3dUa\nv6s4w+SKoQOFpqkhB2VeTOCGfbxZNMbL1wJANReHmmTaIoK+P891NqRd9gglg1HZ\na5TLSN4n/O/xtWOsh2hZDwSH4Qo9HVV4SFWITIHoVx9n+69K1xcJoGO4YwJBANwP\nvYhRCRiiEXQ11r+ObVU3wu4ecHO/YJeDOmRN8N0BM7fzOlakguAWElv6WtpTxp7N\nrgBJgPCNqFZALj4j7xECQARmHARRFnbuTwEapHg8+BLXJd6qo09+N3/kcBy4s4T8\nSU5CqdHSHSFiFmthGrubbpK3fzGsGnTpCpF5dTzd89s=\n-----END RSA PRIVATE KEY-----'),
        ),
    ]
