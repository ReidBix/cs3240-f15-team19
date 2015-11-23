# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0017_auto_20151119_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(max_length=2000, default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDpEcoOgSb7uZByWEiuEsF4Wzex\nezDozVe+EiO3HIsGtk8ueODjIXesmNBAbFChlFtgPoqFjdSXg8Y0mg4rpPqXBhPs\nQ+ecPi2l2drbnPh7XmJ2Cky9reDRSVHAnfHKTYgvyXNh//z5aQyWRvo+0p2poLjO\nH7XxNFd9iIoXs3QvlwIDAQAB\n-----END PUBLIC KEY-----'),
        ),
    ]
