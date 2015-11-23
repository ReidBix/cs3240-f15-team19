# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0018_auto_20151119_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDvWwublMtiQl5ZOj3pBHhQj+dQ\nENoVKs6vY+RBJdO6ZLddUojgdHnJxjUkJUsmPYZepQ1E4xj5kQ60ZYyfSzC+ZFrf\nx/j4f7s5UtPmun8HIuCMcwhpVww0oxmacx28V44x+YfOeGrXtCg2AeUF3ZO7EZ2Q\nPCe8PlZASuel68x8YwIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
    ]
