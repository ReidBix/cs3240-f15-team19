# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0053_auto_20151206_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(max_length=2000, default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC4wh2eH3nSFMlFlDC4J8d1yK3K\nX4HbDxRPkFC/zcSPTP7aQfTXbxtXiFQj2z7eberrhXdOlDhroOzMMq/zwxoMUPhC\nGXZ53mVDnYSFDzj4vBWia40+wTL5F39fERS36u2JTo01EAPgRAsYfzGjQmcrC1VI\nl0Td5J0vCYUzFwuakQIDAQAB\n-----END PUBLIC KEY-----'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(max_length=2000, blank=True, default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQC4wh2eH3nSFMlFlDC4J8d1yK3KX4HbDxRPkFC/zcSPTP7aQfTX\nbxtXiFQj2z7eberrhXdOlDhroOzMMq/zwxoMUPhCGXZ53mVDnYSFDzj4vBWia40+\nwTL5F39fERS36u2JTo01EAPgRAsYfzGjQmcrC1VIl0Td5J0vCYUzFwuakQIDAQAB\nAoGAMSEVJR3zk+SJHOJqDh4t0Ok7JWw+KJUa7olOn6JE2WI9BqaxR7Q4zg7naN19\nG0KZTGWiMxgA5MXXEfmMhkJkI1v2FqlQWqJ0gyR++uJaZXi4jOal7ET1l9F93mHA\n9HZug2HtJf1Q5dC46iVSNXeaUqwaK+V63W2afQ+Rk8/nia0CQQDDd8IMpllCKQMx\nLsLVf/93blk4V+793j3cLSfOLfqY/Ha/qkhNJ5XimynDMP5KeJMq2hK3aF5RyTaG\nhWIIWN/vAkEA8flUalBMDQ0eKpTYlBrmGKCuWfZwswq96zFP/WnUHPDp4+OHQx6G\ncDRaOzJbo7fa13bJ8EX8zDFuuFfrtmCtfwJAaVva17Cuee/bTZ5T3Hqiu8BaDPmw\n01wAYfZg90xnQCEM7OCfGh9VNhDGoPR+jKuTP8zNu9hgxpq7biTlI3SsNwJAU+Hq\nKJzDcHbOsVY+KkGU6I6zQk6TTQ35PpIut5u7Q3kkq7KRjmwDkNwlN4ZCjGPNAoqU\ngK3Sb/rm9hLMjMHBAwJBAJr33+kro3uuIxCW1c2FUEoDj+CcrsQV4HuQ79QtZ9No\nhU1P06qJzaNj4H7TrLed5wxlexsrmnuMlz5loLVeTAw=\n-----END RSA PRIVATE KEY-----'),
        ),
    ]
