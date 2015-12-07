# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0054_auto_20151206_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC0QNNhE8l+H3fBe18dt4Om8Abd\nIQg1p+cR8cSxvPcP493HIkOhjPH1TJb0IS2YlP8pM4tuOJRBrC4N5r1f1oB5qPsM\np6yxrYbbIBp79ly4Bc/LicBLfSmrbm52Q6XKrxK/wVwk/NYoN1NxgG3EXr7h4+NN\nzvhisWdgF2UeWHhnXwIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQC0QNNhE8l+H3fBe18dt4Om8AbdIQg1p+cR8cSxvPcP493HIkOh\njPH1TJb0IS2YlP8pM4tuOJRBrC4N5r1f1oB5qPsMp6yxrYbbIBp79ly4Bc/LicBL\nfSmrbm52Q6XKrxK/wVwk/NYoN1NxgG3EXr7h4+NNzvhisWdgF2UeWHhnXwIDAQAB\nAoGAbAv/qM0nloZeTogZN8LtE4AFXT+ToDYI+GSntrLCla/NHLSZPZky4AsM4UGS\nB0gouxW+mk8n70W6RXLuSShW0ZJKELRn24gv/4bWMT3pjCWMswqbjM3W7UQiOPpp\nxpOnWWV2FU/6IQCoLE46omka9kMbdRTFOCZYAtd1sfYrDsECQQC6/QoQqgK2IodS\n97A+v3Buh5xe8aIRAP52GSAyF4yg9kIqXbWwggJzj0OsygZuRiPOiXBYZPbfm2Sa\nHElcoqwHAkEA9sdu6BLsYQRMxVtcGXM/NBEnYLjfvHjIvLJBoNNj/68VDricP+YJ\nLXVs8cDhVueHlzrK4FAjJhGtPa2zTnxD6QJAc+7ZI7XU0oob7uPk4TKeidkIqZEV\nE4fTPPOdE5GoPlAQe+X39UTWMkG8CtCDJjHUl4R9JEENE1xsBmTNU2MEVwJBAKbq\nrjF62zej2OmEqf7s3Msy7xeU9IBekihPyeQmF3VRz0RtygHObla5Hj9G3yQQ5r17\nns2qZpvRSQR3ANkNZEECQCZFe9ZHT9UbY45vc7cATD2qQzy+uCBjwCW89BIa2nR1\nWm9E+Zh4EjIwFfRHbUmOoL2v32SO3IDdVDcs6AIEpHs=\n-----END RSA PRIVATE KEY-----', max_length=2000, blank=True),
        ),
    ]
