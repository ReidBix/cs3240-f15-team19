# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0025_auto_20151119_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC/rmouO8qUJm7gESippacomVhk\nmRLCE2W5w7/ZOJ5Oib9rSXDxlIVWsMaAx0fppoQX3dXfmyHTQthAb0wqjaeodmF4\nQNjbwKcL3bEEo97aHmJalnA7455HZooWuEVaHhcBIz6a5Qt8oVuqAuWlVU8Rxql+\nXY1MilLoAlD3EYecRQIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQC/rmouO8qUJm7gESippacomVhkmRLCE2W5w7/ZOJ5Oib9rSXDx\nlIVWsMaAx0fppoQX3dXfmyHTQthAb0wqjaeodmF4QNjbwKcL3bEEo97aHmJalnA7\n455HZooWuEVaHhcBIz6a5Qt8oVuqAuWlVU8Rxql+XY1MilLoAlD3EYecRQIDAQAB\nAoGAcGV4k6Wx0w96Ql8tZdTh4NeSUmLD8hNnufcDnv8pLMpu+R02YiIB0eSUcVzp\nWSOwH0KQL68KtZNjtNzOX8Fyhj0O/zKhz3tOQUf5iqbHJMUtfPxK1ITWlEX/+kE9\na18lPPxudVC3IO03TaRnp1qOE42YKLfu3pPHI3inhwEuG8ECQQDYNZpJg2zO+QKG\ntlDdffOBA0ZCJNFHMDaEBVs5eqY8lPhK7a31nwwhiJsVpKPrNOX6b+mSCAuPvlZl\nJdgnKPXxAkEA4vU05XQux0YLYG7v3FmW4SUpfPOoRfsy2UHT8SkzV0L5gWRix0cR\n72Kk5vGB1gmwgaLyPLYMAgKM/f0ZCQTnlQJBAIgzdEddMH1N5maAkX6GapBaRLdE\nREXpPF58lVQnTHObkLJ6+fxiPh0d1jyTI+P2xe229FfXE5lw2TIM3hcFObECQCFZ\nYqJsxgrmEfnjkz9Pssn2ifggXZOa68fc0mXXZgHmh38p3xHlMY95cT22MxveZJ9H\n8ExXe8A327vemvUmUVkCQG3MTn/zstjXWS6/uZYIpsRghYvExcVvqjBVQCesnP4W\n5Dp/f1Wfue83e38100CeDDS8iNuwEcmLhVhvRusLU8Q=\n-----END RSA PRIVATE KEY-----', max_length=2000),
        ),
    ]
