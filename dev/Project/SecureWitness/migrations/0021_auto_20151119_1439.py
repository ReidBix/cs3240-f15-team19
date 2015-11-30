# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0020_auto_20151119_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQClIcikBjdJYsPTQz9WBzMTQDWa\naD+3tAOS6ML/i3x79NE93fhjqblSyySAuA0kNJjD63RbhsTUK6eMQd5HZDgnDVWc\nySsSq3/nyqWuul9ynZ6OzPJwOQC7mOnvPaMwtJRLOTeJpreQ0I0+UhDXK+LBpVTj\n1GkbwdONpDtTH5zlAwIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
    ]
