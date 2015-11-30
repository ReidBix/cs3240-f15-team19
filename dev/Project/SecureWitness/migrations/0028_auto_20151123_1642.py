# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0027_auto_20151123_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='privatekey',
            field=models.CharField(max_length=2000, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCzKLmr7vmx28Sf3UA1UWlx2HPo\nh1oFqo6C3YOMyvQG7Lt3A3t2nIVa2M3HNvxmx7e7Bt3KmRBKEnZC62gnhy9pYhw4\nREqFhiIOnGIasQ3OkwrW0eK4CUZMx1X2NjigrGIL2Bszv4KNlxWAcGw/bILdARdb\nH3vr50Jmkh/KnZTytQIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICWwIBAAKBgQCzKLmr7vmx28Sf3UA1UWlx2HPoh1oFqo6C3YOMyvQG7Lt3A3t2\nnIVa2M3HNvxmx7e7Bt3KmRBKEnZC62gnhy9pYhw4REqFhiIOnGIasQ3OkwrW0eK4\nCUZMx1X2NjigrGIL2Bszv4KNlxWAcGw/bILdARdbH3vr50Jmkh/KnZTytQIDAQAB\nAoGAQuK6ZrECMV99yb0dIoqxVhpcM3yMpD7nk33FhgOjFQ6+chEvv7lxo9f7AxvJ\nIUoAkudeWCvKxAyecB9YtCEpFoviPMQ4mquM8qRbAhtLnpZpIbV/ePSabesF2KXt\nO+tiNN6PrVk0QDNmL6gg8zis1PpsnDqg9T5v11W6FD4byYECQQDRWNcznSkj12m4\npUhYQ1ogqdyar4g5Q/6PFag8YfO70S9M29aevEYZbplq0FINodPKOGG7zBlk1Nma\nxqIfdZyVAkEA2xWsxWmVDOKxA1xTjVmHNO6gDyfnH/Fe71uAZlzgZADtx2+UHNrl\n0lthH2eZBXCtOxTaJ5W/6ZfK3smAISBVoQJAQuLapyAAg/YQTjFowuKKCkObO0T4\nBivmSjsGLHyzTf/Q2AKpOMA4uWlv1QPII5jfvQ10lHbqah/jgqMSK3D9XQJAJ1Dn\ndXHyJqLT42eBMv+bDPu5y558krXtNIU2MKiAOFIWWdEDQn5h+fMeJdWgl2JWJCEk\n2S+9hf0QkhSVIty7oQJADrls4qK22g/NCmvNTzqKzW2W1+YP6SoktP/3V9g9uHdi\nmsezmtyIZ9/LKL9wdbeExRbuYqyfaodtRgjWyfERRg==\n-----END RSA PRIVATE KEY-----', max_length=2000),
        ),
    ]
