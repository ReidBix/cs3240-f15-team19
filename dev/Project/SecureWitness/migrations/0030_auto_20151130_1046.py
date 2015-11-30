# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0029_auto_20151128_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(max_length=2000, default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC+OHJJ8AZtwP6ri1lfAlhrMSLQ\n7NOaHowQ1Ax368SyZ59WhhAKm0iMa0Lc/yf0YvzxfdX7Ls50GbCJVWvbQ3XjXad9\nK8joS6yzYJ9o9LxvXnssvmd6GvVl1CLE8WMf2EmLpauEJFQEwOLrY1H+2wsiqbDO\ntkymSUoU3hGZx6wHIQIDAQAB\n-----END PUBLIC KEY-----'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(blank=True, max_length=2000, default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQC+OHJJ8AZtwP6ri1lfAlhrMSLQ7NOaHowQ1Ax368SyZ59WhhAK\nm0iMa0Lc/yf0YvzxfdX7Ls50GbCJVWvbQ3XjXad9K8joS6yzYJ9o9LxvXnssvmd6\nGvVl1CLE8WMf2EmLpauEJFQEwOLrY1H+2wsiqbDOtkymSUoU3hGZx6wHIQIDAQAB\nAoGAUbJGi7DV4f94oU6JBMAqH2eMD3UXcGLcP0IDVOHiqcjNa0jKzPNiVkSfA/Fm\nRJTbFBC6fVXd/4klA+a3GwW/NDjcCGcbwVqDACXgucFDDvEJtTTemWuDR9ZBOsap\nYP2KlrfRcTO1066gBAZIGRn8H4S+vBWycTdKWLjZV7TZUkECQQDWXs1amfov7PRe\nzwfvrvp13MAruENPHZFhHSTSUMr+8kve+NnyCwGwIriWOj5vOFFWXyu0mglolxEA\n9tn3EG7pAkEA4ykPiraGXf6bAn9Mp+lImK9ks1HHAdyVXFs6dQ4rRqZPf3asXmfC\nS4kDNChNHyr7J7JKwLxTwWgwhNX8NrfjeQJBAJxDvRQHXC3lX/lgl1trxN13zonQ\nJxib6CbPlNDO3jrcKtxdsJnU1iUsGjxANtTiS8BXXcen5aXdQSLfzuFflEkCQAUi\nI2jGESlEnKokyE2vFuXkaMkomu+u1W093odQp6e0EG3X97M2cwyT7w+ZrYx7wys1\nezz5xIbFXPtTfpyZ8TkCQCTBZPRxmNC1u21WiXw4G0ruTfDJRYi3pSCzjxVSe6Qh\nfgorPZ+kBQPogVwGsxQ9LYnBy6KzxU/cNbpbrrdPaBQ=\n-----END RSA PRIVATE KEY-----'),
        ),
    ]
