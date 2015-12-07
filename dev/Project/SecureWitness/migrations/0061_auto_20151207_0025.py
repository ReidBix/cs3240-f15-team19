# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0060_auto_20151207_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDEfJwqhVq4hlERKOAR+Yj/eat3\n6YmJ1xOG7BlscTpqkFTFduIvsHFH5DhdHRHOMy32MpKudj1ba7+BSWH89uqLQaPl\niHN6aPtBGfoqRg3KDf4Q+8nCSGBxf9M/lJaX08t6UI9y2D5TyQ0iAkiJ6kYKRAIB\nGvpHXz8A+YBg7L1ChQIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQDEfJwqhVq4hlERKOAR+Yj/eat36YmJ1xOG7BlscTpqkFTFduIv\nsHFH5DhdHRHOMy32MpKudj1ba7+BSWH89uqLQaPliHN6aPtBGfoqRg3KDf4Q+8nC\nSGBxf9M/lJaX08t6UI9y2D5TyQ0iAkiJ6kYKRAIBGvpHXz8A+YBg7L1ChQIDAQAB\nAoGBALhaemPi7zXGwHUrNuFmkcWyMNG3itaLt8SV7Vyz+C1X8lG7s4kvMXpUhRXI\nWpZvqqYe2UVbp0IJnIr/gTLJsVEGa7Gx3Sf3fDvA3eg9JxUqig73BXwSxsnKkuyu\n3sdObl1RGYl6kTVrk3Upx0vvB4GXWWULA2idekhMjLe5oKlBAkEA2qf8MvqS6IjQ\nqv435qNTNdRCecPWQ0Uzcra5SOraGFhw5mAeF3wX7DqkeA/AG454wCODNMnzG9ro\n0igz7+IKrQJBAOYLVxAmcFRS4nxzGoCXee1B+O9/s51g//q5MR2itMJtqs1mjOYE\nZ7C4m75YGw6CV6zfkHUWV/Cc6mu3x7XaqjkCQDZc6aErF3dk/KxmxDM9jCSn/1cS\nz6SuAdqVf3+XlF3VL0y3vQONwMzkz5tiHxs60t7CdY6cXysfxB7sC+2qP4kCQGzP\nmlvaQrGwDs8cxsFiZNqzpOLr/XKIiiv24uOIrYV1yB+lzSmTldRCTfCnzgx73Kq5\niKPJcMkv/7X51O4QwwkCQF3jedH/xIOuNrcipUwV0XRDpH9JGNdjjAdElZLORaeW\n9gW7i/2pcP4/mNVRxrJimGKLIwYac7UcqenN4TdoFCg=\n-----END RSA PRIVATE KEY-----', blank=True, max_length=2000),
        ),
    ]
