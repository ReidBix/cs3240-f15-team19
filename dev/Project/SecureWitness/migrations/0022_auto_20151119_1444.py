# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0021_auto_20151119_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC7vIh0vEZFLhckL8pnQX7F6Lf0\n486rT44iEzY3BT3cQxXwz6Teqp/96dJZkCrVljjId2BkvSmNcxo1WAbpqVvq8dNg\n6fRhTns3XZOSoYBVDHXR3wKnkLrEnFZIHI3jJFk/BXnOKOihiaUk/0ZzTo9Gqs3T\nhmbfSUfw9U0HQ+anEwIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
    ]
