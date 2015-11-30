# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0034_auto_20151130_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCx70YS7jgQ5RXOQMy5Qxzu0JdQ\n6mmVczn1RcyGT+ugy3qqoGXVOtkKtGE9GlB2H/ripglMK0Ark/j+6brTmeyPxTeF\neW+cPvxPBqurSEK8IOzsJbM2SaZgaVkUfHJZMzOliMgcIw6w4lj7M4oCPxO6bk5r\nN/cj5M1lTOYerbvdDQIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICWwIBAAKBgQCx70YS7jgQ5RXOQMy5Qxzu0JdQ6mmVczn1RcyGT+ugy3qqoGXV\nOtkKtGE9GlB2H/ripglMK0Ark/j+6brTmeyPxTeFeW+cPvxPBqurSEK8IOzsJbM2\nSaZgaVkUfHJZMzOliMgcIw6w4lj7M4oCPxO6bk5rN/cj5M1lTOYerbvdDQIDAQAB\nAoGACTvajhbwr+fDhu2T8jVKZhZLE/bmPcw6AMF7iKjTGIgWuI4UWslwA/8yYKJh\n9I9aTLLDHsHL1bcbH9dvS5XcUc9zCmyb1xLs7FFzCocn1cKF7npOJNYVSr20KvFR\n7nEPuD5j/NAQjDepvuB4eGzb0SLJWpiFMYOxTiXybw0gNR0CQQDC6PDrSkoWZrdR\nYpxm6yaO+M1d1qt+yKiHZksQubI/3yqHu/tQICG0vksaCMp87m3aoktgnQE1hZYD\noUcX+jXnAkEA6bRIQX+/GEAj/LECq98ny++t2tvHXopBQRlaSFpas1YwU3PpuI8+\nZTunbVTj9LXSXXCOMwyaTOnh3AFmCGBO6wJAb7zhGNJ/BLagE20n4qyeb0pdWZWO\nvWFFlFHlaNI8SPekRypSWc4B5L9PCL7Pbq21lqiB9AIuRkOuC6iyvCE6MwJAVuKk\nnl1NAUoPVwnEEXv0grhH7X8aHwbNfdNcIlwdLmFTtCL6+JegvegwtdACs97JJ94J\nr+b2krO9OZr3gRO1IwJAAeUNZr0PPO/ODoT2bCybNJMtZrSvixNO1BhaNHKlSLbe\nLwl/44snRTOYiVewl4fg2pY/izL8InILDkQcUJ0umw==\n-----END RSA PRIVATE KEY-----', blank=True, max_length=2000),
        ),
    ]
