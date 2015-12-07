# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0017_auto_20151207_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(max_length=2000, default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDA/zONWzgMRPqamJzgPR1PLo6s\n6yFIMO13H0lQZzwBd9QkZQLVvARlyaxiJKIk63/24e5h+mnIwa6xbMfmjt14e/pE\nflMpwhvJbYAMKeggEaLtkQi1GgR6zDL1NzPHgEYdnFCub0XMkliJd6x2R9stofHc\nfYXJn4wmTocEl7EM+wIDAQAB\n-----END PUBLIC KEY-----'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(blank=True, max_length=2000, default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXgIBAAKBgQDA/zONWzgMRPqamJzgPR1PLo6s6yFIMO13H0lQZzwBd9QkZQLV\nvARlyaxiJKIk63/24e5h+mnIwa6xbMfmjt14e/pEflMpwhvJbYAMKeggEaLtkQi1\nGgR6zDL1NzPHgEYdnFCub0XMkliJd6x2R9stofHcfYXJn4wmTocEl7EM+wIDAQAB\nAoGBAKYT9fzSXmzQfwbCBV1BuhMFcWmD/OPulqpHlgNGkvCAeWHIOqRKY05kOZ9K\n/uzeawO8cDKIFrfXU8kCXxMcJZ+kBocTT+Ak2pUNgBy3BVJONN3Yoycl7V0KF0Yi\n2yxV1N7QIeZvjgxZ2T9klBsmTr5lD3b6B0BzYr6BsbeSTdZhAkEAyCJVm8bbGHMQ\nXF2MFRdBrzPdH86lJy+pHXQMOVETf7Egph85U8Ph5PV+mZaDiAZwVgdfWpUH0x51\nE8HY5dpTRwJBAPbe1kYAHfrKr8UfeeTDLAulSB+7c8pt0TssSeyKFLjDquwhfEqI\nYZJl2eg4RE0RdE4WHuSrPVQ2abAQwPvqCq0CQQCgmzUaUuXmZAiAJy5Qip5SrItK\niDnvDYdotIVOxeqg8ZNi3PHTcAHrDLuxI6GgWpJx5261MZ3a5blMxqZ6Js/nAkEA\nh5Tgx3ce//K7UB62Wj4afZbbopnXwRBI/h+XxfIb6VGFGMRXN7PpKncHkzL7x/vT\nDWO2uc2WFB8CMnExG+lwzQJAHbCRJ9Epeqeu3orkE40On6PM+oK9I1/AV8myyIUS\nFo2Rcn4KbhVacLku4q8nfKC+iusmIIVMaMoqrdU46HWmMw==\n-----END RSA PRIVATE KEY-----'),
        ),
    ]
