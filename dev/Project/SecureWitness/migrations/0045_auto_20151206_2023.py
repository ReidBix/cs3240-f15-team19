# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0044_auto_20151206_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(max_length=2000, default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDPHjWL2y+R3zwwR4WcXKs9RDbN\nJ8us9Azl/jTY2D8kVWa2QahNgw2JT2tx09zgRhKx/5PLLXJimb4Yfi+o0VV3t6GV\ndoqDFFkTSqBsUFjzSexgVQdtZP8jyqrMnfmBG2Km1uh7aJ4xLKlLXbuEt6ec3Nl2\ndqgBXB1IqPanKOh6LwIDAQAB\n-----END PUBLIC KEY-----'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(blank=True, max_length=2000, default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQDPHjWL2y+R3zwwR4WcXKs9RDbNJ8us9Azl/jTY2D8kVWa2QahN\ngw2JT2tx09zgRhKx/5PLLXJimb4Yfi+o0VV3t6GVdoqDFFkTSqBsUFjzSexgVQdt\nZP8jyqrMnfmBG2Km1uh7aJ4xLKlLXbuEt6ec3Nl2dqgBXB1IqPanKOh6LwIDAQAB\nAoGAGSZb7i2hax8mWd51dPUzve7IkMTiUJAZ+NuTYzlvAWR1YnA6lZ7yR9gi/eFy\nErGvl3mnYqaUGzD8ClFYTDGPJRBAdlohhufnfB+bnFpe4kj4M8vCf9vxD6hVznJx\n4exTzFFPnxx0wX2EzYv6n231tIRDlN9myzqovmljns5IlIECQQDTUrEIceN0zESu\n8dxMPpz8a4Bl4vzv6Dh7w2qXxEAO2M/KAWVo544gz3fFAaeSTcCbFjKM6Q6LCMrQ\nuBICJc3PAkEA+ufutHxQUCUHgwyPsedcSna/xDg0B6+KkEnLZsS3KpfYTS2WKEAg\n4dQx4/7q1MN82E9bPG4/p1NhJVHxKFMFoQJBAMAvihVWDjhgtW4tQ96LaxYdZm5C\n2yoMFaJo/H392wwlngPm9SVMwXOReylN8eoakDn7HAoOwk0rt9fOL4KIgv0CQDBz\n+bUBDMFtZTX5hwZkF36J0B6ke+fADpIurgj6lCS1jh/ZXdYIDFGQGNJeuBq+Za2g\nJY5V/BTkFS6P1HJlFgECQBKD8sx2ilYrwmCO7Ixm6jyy7srXOhX0NFYpZeuDTDbj\nqb43F37cmWRuy4lQnt8SsJHvSVsz9O7ipsP7P1koy6Q=\n-----END RSA PRIVATE KEY-----'),
        ),
    ]
