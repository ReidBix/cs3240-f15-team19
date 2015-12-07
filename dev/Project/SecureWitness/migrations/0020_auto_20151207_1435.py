# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0019_auto_20151207_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDX/Sk2d8FTFQRn2N/1NQdYDTBH\nMMRlTw0ye+8RQiUlEm1nXrUMZjEOjQ3igmtZodor1MQ8UjtRMIKmbf8xoxHyLL42\nqpjRwXaCL4JMQ2cFfZib2Lfkao+5/0MYFntDi7x69zYVzzZDkEH8ld7iEaoqYVad\n12csu/Pt8nmV0/POkwIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXgIBAAKBgQDX/Sk2d8FTFQRn2N/1NQdYDTBHMMRlTw0ye+8RQiUlEm1nXrUM\nZjEOjQ3igmtZodor1MQ8UjtRMIKmbf8xoxHyLL42qpjRwXaCL4JMQ2cFfZib2Lfk\nao+5/0MYFntDi7x69zYVzzZDkEH8ld7iEaoqYVad12csu/Pt8nmV0/POkwIDAQAB\nAoGBAJ7nimKgSIMve0ZLsLlegkCts08s+dDvD+6Mb55q45karZLXgqvUo1LpQ8XZ\n3dDb2v9UUetvNGTPI8/+LTn/lzsSKGzobeGGmrHYkxl19dBL2BR6aJp7OGNdyU/V\nOf8ytLUQrHW67oWa8XFHXVrXtC4ev5J/RPUvYg50oHFKj/ZBAkEA3H4EdgnNq4od\ne8u/Pf5Jnyev8jAL3RWJ6FHImVmlhEUQQ55iIt7+oZlJOvf7VbXDcz5oqCfYdfYJ\nG2kR/KS6RQJBAPrFfUFJWIDP2PCugx5jeeVHFNVtso8pPKwMoolFBLXD6pv31RrM\nEvknzrR9dx/HAd1/tsiWQMEMInqkxAFwHvcCQEAMRwV2sYybsRbNx36diAs4Pw6t\n0DRnVkjqwMdy1/aFDUVnE4Cnn/WXDkOX1yU9iEnIniQCdwlE775LlhL6UrUCQQCQ\ntQm0dNinbEkpieqLzKd4kO4KwwR47Djgp2HbiIJRST7GxdqpXf3M3RXAvW3SXopL\nAPm/AkVXoOL8lrusgMC9AkEAtZl/xh9d8mXoA05DMUlKEsp+cDwK8ytRCDxZA6Bz\nGlZHHxQgtF+S8wfaXAcPZs/OO1Og0OlOZMtklzPXhYrHfw==\n-----END RSA PRIVATE KEY-----', blank=True, max_length=2000),
        ),
    ]
