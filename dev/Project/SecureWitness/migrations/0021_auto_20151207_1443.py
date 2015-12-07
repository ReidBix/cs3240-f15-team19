# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0020_auto_20151207_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCNezwZhwUw9BvdBN2kK5bTkSpI\nrT+zOIQollcssOS/zrINae4d20RVPhQys/8ZLRyzwztrQAQIY9siDtc0J6bM5qjp\n5ADPvOmLAH/FDL7S6Ri18mpBzmPtsJvmloBFn6wf/zG/Ext5GW17GblPKs0CrKxF\nUcWwWAtS/stwAIqRvQIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQCNezwZhwUw9BvdBN2kK5bTkSpIrT+zOIQollcssOS/zrINae4d\n20RVPhQys/8ZLRyzwztrQAQIY9siDtc0J6bM5qjp5ADPvOmLAH/FDL7S6Ri18mpB\nzmPtsJvmloBFn6wf/zG/Ext5GW17GblPKs0CrKxFUcWwWAtS/stwAIqRvQIDAQAB\nAoGAXVcRVnIavao++7jrFRVg42GhOON75ByELFbLWoO11slh9LGPVAlF8ssK/kx8\nHzsA9aP2/pH0Vyix+K0703/ZbdgC/jn7qaMdZ67GKA4vgI0K1lZNFRQy1js0Avh6\nj0EV5mU13lv2fc4HLk/naQkRKQUFKoygG9EdjG3KolPh6KECQQC47MKv/TzdmeW1\nzuUEHSKMHPAaP6r7NSthjLh+M1miGy9VDVXHgrt5BAedjMr3XizMVx1R7BlZjfFJ\nGxlcmvf1AkEAw9v1ZCOqwJ+B4k0go9r4BSUy5NWibZrfDGUbv8xerHMVlJtE45Lz\nlhF6HzBCPWD66oV2DKKWoCyfuQWanVm9qQJAUWzm2Mkf2M+f5ur/ykzt3lYLnvMz\n3ULvJBfrUJ5ZtFhWAhRKFfxJgiK1G7lX0Y4lGaCuJ1lXXCh0+uS0ySLvVQJATJGw\nVI7REW8KYwNOEGDpd3F8fRO75WeXbYwVlhz6oiZ3uFofS2zGx9NbT9gY/U/tqEO2\ny+fARSxM4RN8x6kuyQJBAKe3xndiBqIxrvhZ/aQujr9+57fVgV2q5+6h3O+4BYrb\n3RRZ3SB0JbvrISvRFdoJXOhS2oOYJF+RWa6APGN/hls=\n-----END RSA PRIVATE KEY-----', max_length=2000, blank=True),
        ),
    ]
