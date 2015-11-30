# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0036_auto_20151130_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDbHTzWRF7WA7vakVMuzafh4Oob\nhzAmbxWJepD/jDfE+QADaGY/L7h2WiRXbWW+bXYAMcaSHQFgUzOs31zHq2dRDSic\nRGJfjb9OhXS2NXZHyUu35w/PEDlH/rLTWLs6GqWqnQIgpL8mjUbLJFQPV/cuWqkC\nHglqsZHCCtf4dahhEwIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICWwIBAAKBgQDbHTzWRF7WA7vakVMuzafh4OobhzAmbxWJepD/jDfE+QADaGY/\nL7h2WiRXbWW+bXYAMcaSHQFgUzOs31zHq2dRDSicRGJfjb9OhXS2NXZHyUu35w/P\nEDlH/rLTWLs6GqWqnQIgpL8mjUbLJFQPV/cuWqkCHglqsZHCCtf4dahhEwIDAQAB\nAoGAcR9wKEMWHzHAS4BZzMEaWpCO7PVnk4AoQ1kHARg4NrZDHn9Iwnh1qIyzVHvD\nWoQSttj75rWY3001UZvjv6YraQVRJIlsnbPhPi5lF3GnGb5Er7SGtOz2PVx+FmSb\nRB+cbFs8ytPJ6ZaHN1ToYmx5dANUsHiIltDrx7QWKypgcUECQQDli8UgcRWPsJIm\nr5SZ76bVfOy7iNnrOk+g7lcOsNlLL2SghAnh5Wpf6f1LyH4WiQBhouZWaeMWXY3d\nlCBY8QjhAkEA9F2zv9OLrYQ6016edzof5ORGKdY5egur2C8hhzr8KqrlZF/Wyuzx\nT5Aaf1XI67Ei2igDizUIpnsCsBG5Z5nkcwJAFfmVe4+X4tOiijWQ4lPBAvscpq9p\nPU2txdhLWUqw4rO8zGkXkRqnXltGNnURLRMciDxSFL+6T6/RHv9JQXqBwQJAHj5G\nk9QrslLuMODB/gGMlviFkoH35Rnyr7PNk34CXYl/EHgoDj9a8jzkeqP0VO88YAGZ\nxq3On0QUJhRbfO337wJAXb1BgISef/8Z87N4UJKtjjCGJB7F9KYVtU4L1tdSs9eT\nGFnSzhUimUMO0004GTh1QKT0czcesZGLhFMIkI9nlQ==\n-----END RSA PRIVATE KEY-----', blank=True, max_length=2000),
        ),
    ]
