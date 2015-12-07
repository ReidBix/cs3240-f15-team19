# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0045_auto_20151206_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(max_length=2000, default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDWpCCdKZXAHvdxZQ49cIS7bEBy\nMSIZIpcailT+RtjROP7DisQUCP1IDqfnVKgxF4PupIyhBmWPZkEY4qp3/oqZv4jt\n6yc0MGk2VDXtcNkO1MlcL8D1Ra6C9lN3ikn6oDs7NonUxVz1RAP0TeOERdbmyabC\n619+PmixbuuDjtcPnQIDAQAB\n-----END PUBLIC KEY-----'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(max_length=2000, default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQDWpCCdKZXAHvdxZQ49cIS7bEByMSIZIpcailT+RtjROP7DisQU\nCP1IDqfnVKgxF4PupIyhBmWPZkEY4qp3/oqZv4jt6yc0MGk2VDXtcNkO1MlcL8D1\nRa6C9lN3ikn6oDs7NonUxVz1RAP0TeOERdbmyabC619+PmixbuuDjtcPnQIDAQAB\nAoGAbjorZYqNlPRSLrGu9m5qO7YEAqCo2i+hWcfgjhTkE84pR1JkD8XuDKs6Htqi\n5VMmNc/bSHZ4gYQJujXtRWI62nljo5NxWzdkQtiISosSMPeu7ie3hM6JBsjDOg5y\nLXx0brumna2eB8I6BIKIJYdPDWq1gOd8DfI2WS7r/Dly3yECQQDkldNiIh9fOIL3\nNDtJsJ21Tzi3YCeHCzXkDiv8yRM7ZnhRW5swRC+zsdlQl7K29oXWz+IURZGVYRWt\nJUAmraNHAkEA8GIuA7f+S+47/4QD6TyNhq5deLM46wPFLXStNLCUxMdJ+9ZYlY4s\nVs2U5nEPFSPEACS9cqjSclpXBB+hIwq/+wJAFwUfrJpTHnvKdKrF7b3jpAa+Z3k/\ngdIXM0haFbMKRMklBMx87Hdxdl9Ky1r7nIFnKSL2WaRH7QtB65X8x+hksQJBALIC\nwriWRIbOQTgS9yJ9aQDXlviPIBNJk3b59FoUedbPDgak0KzPwB3319Be4SByf+7r\nRi/mvRFZvR6cnaNpjokCQFWA7j8Su9Kf2CMGgjD8OWIwW3DzJYvU+u3cZxTxgllk\nDUFre6AYlDB2HPBtM69ZXmccz3MdbigmRexBW/g5szM=\n-----END RSA PRIVATE KEY-----', blank=True),
        ),
    ]
