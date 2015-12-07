# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0004_auto_20151207_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(max_length=2000, default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCkrJNUR9waLdILDqUusV5TmQ78\nxnyUtRciInWQ9hDd/MHeYve+GKNeEXkLy0la+tc0V1W5nqD04OEWoNnFSa5Pncal\nSCyxcZ8Y9NhS/2tl9xYSyMIVcdJlHTXqasiOmFcK3ppfNejKA8wrLFmjcLUcjQqN\nsEtvX8wZ/W6cMQ76YQIDAQAB\n-----END PUBLIC KEY-----'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(max_length=2000, default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQCkrJNUR9waLdILDqUusV5TmQ78xnyUtRciInWQ9hDd/MHeYve+\nGKNeEXkLy0la+tc0V1W5nqD04OEWoNnFSa5PncalSCyxcZ8Y9NhS/2tl9xYSyMIV\ncdJlHTXqasiOmFcK3ppfNejKA8wrLFmjcLUcjQqNsEtvX8wZ/W6cMQ76YQIDAQAB\nAoGBAI5/Q7IvyLfipJqq3qeMFmrSzNRR0eZA2jbQiNmbBLeDjCOrkmQuH9g72Hor\nPFv9KhKB7I2GRhQBMOYK5MdC3hFjb6UCYp7ybqkeLkRtiwDswMMkOpvfl94/C1CX\nm/DmYbTPZhtrKwNEnLiUtUf5pY2x/28y0Bn991CLp0OFZt1RAkEAtxCtMNoj7Q6L\nJtqNTzU80dB4L2lAXwVpndouuy3NPMc72UBo7MwCQxXNE5fjjmg3aiuM7L3oClhR\nfx5iY9st3QJBAOZIJc9XkQVCZOA6AX3/xcXgYmX37WYrJu/txoQCYQi0+h8HMALH\n0poVy4tEW53lRaHI7ZY4grvNz3V2Sbu/wFUCQASoDO+4LL/D5fA4EO4Z2ZEwr03t\nbHC+T4BvY07pjFXmb3RIOiMD0W7paAz+iRA/QGGX9/6xmexhcLk+CZymn5UCQDUQ\nnxXeed6aZCB/fWSJkgt9H2+b6CrI+toDEuHMooudGJ4Zy+h4H4G+T/8xq2MBOECF\nyqn5L7cTQCEzNt5621kCQDIkVaWbHx4VuIHCqYPtmP5BUdTy2PUHkteer9q9oyt/\neKHyyC2F5AWzBbPdqoE0Cf0uS1Esr1+p7ikcNwHLcVU=\n-----END RSA PRIVATE KEY-----', blank=True),
        ),
    ]
