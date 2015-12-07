# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0057_auto_20151206_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC8c49UGI/ue6+ZwGHw4iWf+/Nf\nZ2m0FMy+VoKUlmsxdOl+zCkLKz3eVkwvtp+rj62rhxG6qPcS/Gl5he0lIr7PzYL6\nUSmwtWKpbICdC1n66qUEvvmzDPdKxAqGeVlSWfz+uLEWgc/725SPggin3vFyxiu0\nU4V2ecVTbWwNLuG50QIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXgIBAAKBgQC8c49UGI/ue6+ZwGHw4iWf+/NfZ2m0FMy+VoKUlmsxdOl+zCkL\nKz3eVkwvtp+rj62rhxG6qPcS/Gl5he0lIr7PzYL6USmwtWKpbICdC1n66qUEvvmz\nDPdKxAqGeVlSWfz+uLEWgc/725SPggin3vFyxiu0U4V2ecVTbWwNLuG50QIDAQAB\nAoGBAK8EX8uJWDrzEd2oJw2w6aKQOrGS+D9vxcrLy1A19m2jF6tT7pZZ3Yac/Pqf\nD+EkefVAZv3FKFmwpEBhWiHQCAabnxD2hbwZB73Qx1vt8Q8G00EUzK8LwAUdQJ61\ns1gjY0knT2NnAajAAhugGomCPTZUvV2xy3XaeR75LT4WAY9xAkEA02xUQhUd9tTk\n6Uj2hiYmAXw4zA6Pq0IpxXC+C1XAhc9aJiY327GB7CSITFWkSmJtIb1CJOkw6FDF\nStNrAiuExQJBAOQvUZuWmIdUTA3MAs/dHsxwfST+BiB9Ek098cYO/EjY+jehjMKS\nlKDPiTixevx5WaU05KG1MaclWX7UT86S6Z0CQQCNwrowYQZpZdBjV4fs5RFgt5FB\nyZWtiDyH5ZOX+BSR5DmXENMtXLU3yDsXq+jv81UnZUY/h5hCfT38cQv0NYfdAkEA\ni7IUagZmVuNatE+joRIkWtC7LLx/j8BCRhuYOsLN3ONJPGmgvTXz3AdyYMz3GD5K\njYO2PPGq9kM9aRId0b/LWQJAV1VaQOqBd3cjpbNOXalm1mmGl88wtzfepkkdNAOy\nkYiNGn1giov62kKRQgBwqQkKunK3HfHPeOFn28Or7dTVfQ==\n-----END RSA PRIVATE KEY-----', max_length=2000, blank=True),
        ),
    ]
