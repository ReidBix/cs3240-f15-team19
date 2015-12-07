# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0050_auto_20151206_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(max_length=2000, default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCMFMRpf8jnz/bmogCQNYt+HCKp\n9g4XJ7EbX0TSOaly+wb54/8E+IuzicWU+ecneSIZERRIA0AJEFLccPauKeL9xSq0\nVz1bHyc+j5HkbolDwYePzu7tmffUaVcuzGFZGYm9hlDwbRbdZIYt4nMXYmtjm8Hs\nQsGfmx2VeXEEh/LFmwIDAQAB\n-----END PUBLIC KEY-----'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(max_length=2000, default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICWwIBAAKBgQCMFMRpf8jnz/bmogCQNYt+HCKp9g4XJ7EbX0TSOaly+wb54/8E\n+IuzicWU+ecneSIZERRIA0AJEFLccPauKeL9xSq0Vz1bHyc+j5HkbolDwYePzu7t\nmffUaVcuzGFZGYm9hlDwbRbdZIYt4nMXYmtjm8HsQsGfmx2VeXEEh/LFmwIDAQAB\nAoGAPTFRP9jvlbx2WffJETYi0ptN1TtEmn7fUlrCwKcpy623NXCQ1cYRmQOFSXgF\nr2uuJo8ccfzhe1QjLmM2j4yCuL1p1sGcNoUyPd5rkFeV6lxZTOmGkINMqx+1/hfD\nJECvAfyf68XgPjy1q3De/pyguE4bpezTpBp3cuQVU+XdiTECQQC4wqCRfRt6Q0n8\nYct8Zdw3am4eeVnF31ayyS6P/EKffEGlkYXqpDg582ZsegDvBbHErXrEpT93RJpG\n3CITZKIzAkEAwhfwC5RFUY/vmOgpTKWQfc3AVJ7xVgVjIA0YVjVR0TwTFxIyho+d\nvrBt7cqqYaBmPwWZbqUkzxvBu01yf/z2+QJAWQ7Hoxlw80AYG6VwFmhq+/M7XUkV\nMsHy4n8DCLiJzKJyakJ5EJ9T0us2RbeRV6WhCLKuaLdWnkDdNKbLbhml7QJAeLYY\nhasOPX6uPcPNw6yIo6UuA7LiV2R8VLewNhVtMBsTqFqZ79QsACeMBsLvmk3+qR1b\nYlP1A5W4tDujhXQXSQJARVFHXXC+IH9sPbHoaM41yr2LbxYB0QLD7i0wRMLFxdCk\nF7KSsMCybKvhcKaEwBSxO5GtIXYZn5L/24d9CKjHWw==\n-----END RSA PRIVATE KEY-----', blank=True),
        ),
    ]
