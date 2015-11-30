# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0031_auto_20151130_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(max_length=2000, default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCgfE05puAwRmDg96CpXlQIgLaY\nUyik7Y0Q+cTcaiqCs3ZU5XXR3mxrAxvVQfgu0hYrys6yN8BYxQxoI3x8Wgh8VHsq\nTzFO10oFwuw4C1vvjksuJHiGLNvNdf3UUdrx9m7CpOdTrm/B5wUYoaonmMFIDjlf\nCreVLw3KhrqahdtGZwIDAQAB\n-----END PUBLIC KEY-----'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(max_length=2000, blank=True, default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQCgfE05puAwRmDg96CpXlQIgLaYUyik7Y0Q+cTcaiqCs3ZU5XXR\n3mxrAxvVQfgu0hYrys6yN8BYxQxoI3x8Wgh8VHsqTzFO10oFwuw4C1vvjksuJHiG\nLNvNdf3UUdrx9m7CpOdTrm/B5wUYoaonmMFIDjlfCreVLw3KhrqahdtGZwIDAQAB\nAoGAKn7/zAZeUyovuSKZToAF7IJ413kdyB6HPjmFYYBTZWy0JuLkAgDN4MBf/GaN\nm4hSCqKXfSW6L0duc50B98O3fxjeG0xZrnfyHOZMgSW90SVrrA19A2t/N/mhqtmn\nqLw8kFr+phsygKt/qxV4Xv+lOda0N7DtuMg23b/gl9Qr8CECQQC3+yYk9Qo9stX9\nTbKyWwdesBqV/RL1NFKjMA3/NSIVepAWO+duHsFjdQMfCd5aCY21+4BQn/DV4sZ9\n6X2BxeiZAkEA306nos0HTDHjrUmtd/Ax7QjHAgfm3Nz6Hhn5fdU/X4iIAV0TTRUV\nMhlpyMr//POZAcvVgUcWaLEjYq3F0o0G/wJAHFB0kF990f0B3dflVnmX6sSjcs3d\n6wrAZQjyPoKI2lFgd2uEtHfbP1k0v8QfCjBKNOWd28qhn+kkryAOBrjUkQJBAIbI\nzew4/q+h6T+eGgMryqa8xonWRSWIh7uFiA7ImSDLovPXvx+mmw2LQ0t8I/kE+5SW\n+L64LrFwQeB87MuCbfcCQAykZ1mFjHIPN7BjgmlGqewIq/KzPVVM0HUotFk8V+tW\nQ5QHHG9xO1La9euRgB1DN86o1wP8Z5RpIUupo00Fu8A=\n-----END RSA PRIVATE KEY-----'),
        ),
    ]
