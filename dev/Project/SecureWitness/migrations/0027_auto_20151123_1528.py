# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0026_auto_20151123_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDG4F0kiq1dvCi3zjVUujAwbLJU\ng/45RHh0sSoXFjdjFvVqpuRKHOk8SvzYTUi9ZTbVIphBFviwQpdNgnUndFmntzpB\nqcvEMSXolJtmnW7d6zBOTOFrE5mrteEZLptOLMLBz+Pr7Q8ylxSclx4RU65sJxOm\nwa+kFa/8kHz59VpvCwIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXgIBAAKBgQDG4F0kiq1dvCi3zjVUujAwbLJUg/45RHh0sSoXFjdjFvVqpuRK\nHOk8SvzYTUi9ZTbVIphBFviwQpdNgnUndFmntzpBqcvEMSXolJtmnW7d6zBOTOFr\nE5mrteEZLptOLMLBz+Pr7Q8ylxSclx4RU65sJxOmwa+kFa/8kHz59VpvCwIDAQAB\nAoGBAJq5NV3XkjdpytftUyp+zDzwY/FC24dcUMagitl5TFAILZjzDIroYUCqKnpx\n7hSDaRx6lK+XGpWuyR3hUBoI+DIW9OPubjc0VN/Us3DCQeTxkRm+ZjkSpMIL4vcP\nmKOwQ6AWeCaoF8Om8WjJpTFHcbnLngax0ET9q0nbPNDbYjmhAkEA168sdbArDpZu\nFE0+rZ7TUwy1MITxONP2Jh4j5TUYZXkT2vxFYQpCBSAcshxewOxDWMj+g3JlMnGa\n6Vtxr/I++wJBAOwM6JI+Yn1sTm9bwqMI9QhD6n3ph8sRXEl1gt94Vs0j/bAY8eyf\nw92ZdlMQiN8hkfOXuzUzqrJMdRdRwJ/jUzECQQDQ4OAw1bzNMthGpwxVfqRwILV0\n2Lr4ayZOghAHUWVgGGMnR/s04IdRiWjhAWKueeE7IeSCjo38zVLWPm4alINzAkEA\nwGwFarHQN84CYmS61YyHsqUqklm8iJ0uTfOtK949ZBziwJqVG/9g+1QOUMg5yyri\nf2BBC62CiLYq/Ud3bt8xAQJAfg2Z5MSCtrdGm240y0y/l9p9QcYMnQjEvdeJXZ+Z\n8v4VooQ6V8sJSizhj3YoRSZLnjTk/nPy93oMgxsy2gWGvg==\n-----END RSA PRIVATE KEY-----', max_length=2000),
        ),
    ]
