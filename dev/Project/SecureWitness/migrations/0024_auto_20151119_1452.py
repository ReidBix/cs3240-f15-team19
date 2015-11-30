# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0023_auto_20151119_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(max_length=2000, default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDScWVkKJdWA+Amd/pKDagflRRb\ngQ1NDxhYns7y6iTwZaV6N8MjpvOIeeoml/1PX0DAlvvyT3/tK7k4AfeMHtEE33Ye\nUaWWtMoctJaKzlKoGz4zg57QuGU2efmOowoOrS6djvptRjyqDuWQMg3RMQqcgpJC\nd07s1Qjyrm8EQppUGwIDAQAB\n-----END PUBLIC KEY-----'),
        ),
    ]
