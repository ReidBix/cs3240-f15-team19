# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0014_auto_20151207_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDCPZjIB/ga0Vpx3ptPDvT4h6DY\nbK/MEjNPAlIUFt2CdaF/mhQ96ZhpgrPEzNfze03G+1cuh6DSwY2JK8HPJ0uQ7qPh\nvcfcu6vHwHHSF9EO9Npc89dovWtBVX9fK9nIW80j3C2bUENWwble0wAvqHNfloXM\n5rFxjZuZhHh6qNbAFwIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXgIBAAKBgQDCPZjIB/ga0Vpx3ptPDvT4h6DYbK/MEjNPAlIUFt2CdaF/mhQ9\n6ZhpgrPEzNfze03G+1cuh6DSwY2JK8HPJ0uQ7qPhvcfcu6vHwHHSF9EO9Npc89do\nvWtBVX9fK9nIW80j3C2bUENWwble0wAvqHNfloXM5rFxjZuZhHh6qNbAFwIDAQAB\nAoGBAIhQxCz1csgXTlsFd4dXHtJgFKBuPj2ANGPpZALXPSM2PF2Zm0UL77t0T4b4\nn0EvspjHgRqVcmcWEKdIfx5LHHri0BKWbedpcKK4xNbLYC4cU1K5e59NgAFUALAa\nKM0BBqZuhq6PWFq+V8F9Iok3sOrYkiBOPDs4dSWcDo7qh7mpAkEAy+Q7YZXXPp6+\nW9a/Hj5JAomm4UZq3o4+lstC1PE5V6lf0pgtMHX+Gai76qS+vEAvznWipn1tCods\nrYA7umbPJQJBAPPh8hmwd3Ok3ezjQdy66bjuq5e7h1tz0CTQG3/22fVog+d9reZp\nMhRti8ltKsRHhaV+Er+1JdUMVneZjlvP+4sCQQC0X/LQf/jt4w3QvYhSPxPj9Nb3\nkI5W2Uwxpxw2ujjafnLRIeNIbfofxRCJorlCXR5t7c+4rlla6TeRvlIYs38pAkBb\nEj/O+gfRRnqdEEwy+hV3OqEXOy8Tpo7OgGwUgADqVIoVMuhyh0vtNu8hW8PBohe1\nMfwcXK/w+/d6F/yCKot7AkEAyTtCHSRJ8kPKVzJ5asHr+FmcGfOOpQGIhui3ZRel\n4vLsYE3J1E8fIeuTG1bStAduk5/3DyVpNQ49XWuAbNtcGQ==\n-----END RSA PRIVATE KEY-----', max_length=2000, blank=True),
        ),
    ]
