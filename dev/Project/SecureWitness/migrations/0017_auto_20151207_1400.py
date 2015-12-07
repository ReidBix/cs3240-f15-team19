# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0016_auto_20151207_1359'),
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
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCaAJhZljQ060FyaCy6esGE1ky/\n/JZh8FX//AmzZ84L4BxJnliVwr2a4G0DsSQle1VCScPUYlRq9PwCOHI+lgPnJJXQ\nUW8Caia/g0kozZQn+27/kisiQwszrK9rPRf/RdFH8t+agW/tDAGBUkungbJDZR1l\nq6hRH6zjOO8RPwdo2QIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(blank=True, default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQCaAJhZljQ060FyaCy6esGE1ky//JZh8FX//AmzZ84L4BxJnliV\nwr2a4G0DsSQle1VCScPUYlRq9PwCOHI+lgPnJJXQUW8Caia/g0kozZQn+27/kisi\nQwszrK9rPRf/RdFH8t+agW/tDAGBUkungbJDZR1lq6hRH6zjOO8RPwdo2QIDAQAB\nAoGADzOB1k36R0L1idp4l8uoMHmKx+Sh33b+ti7lsjzL3OY5RJcJvXakipYejJ++\npqh+6PUpDFzMYmZePcXemQjrx4zjt0Kjr39muutfooOL8PzQOIyImWYUoIv5kVkx\nFrV8TeNMO4xGlRBdstDVrbZs/3VSd5R1kzo7Clt/p9lVBIUCQQDDS1aFNtQCIUJj\naNP0PWUiinQFQ0wTEiKhjddMmpGDq8qkgJ5nhYgpFnkzVo+OakbtWYsIGT4btkrr\n9W5e3zofAkEAyd9shs9Yloz5qGHmJ7c4RWUGg7f+w0OO8SqgnMZn6xq184uhLl6v\nzQD83Go/o2ThHCfcGyS2qLJOwIdfzJzuBwJAJgYNGnLKZH/FRUWrvuoVPtxmKoAn\n1664P2w2dxvBKTnRgqXoMY+2KwnNH0nDOZ9Hn/7HKxR/GzYq8DYg/yfHUQJAF/+e\nmDwoDOW/fDv/L3OBlgZXiushtzbd1F+77kdL7VAkl0pfI/MPtTBL3ywmWpdQh5dZ\nfESWDmH8KLkvM1TomwJBAJCTc0dGtBH9LCFkt964pkCG9HA8N0cq2o6P4vV+kYmp\nlvkvhwoy1jgkHsqE650NzOx8C3rhemUR6oWGonUijcc=\n-----END RSA PRIVATE KEY-----', max_length=2000),
        ),
    ]
