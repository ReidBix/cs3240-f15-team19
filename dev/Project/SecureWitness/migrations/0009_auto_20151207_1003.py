# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0008_auto_20151207_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCcbT6fcGVkx/r6Hx3UR8nP2CEt\nR51f3IFmHxdOpEa4tkYU91FICjhhyxITTu61ZVCDBJfFyLu1XlXPtAYRehIJBJdC\nZJhIQyeruEVPzEUn0Igiaz1YyCATXPeui5U7LLQDUm4NImHgNYRjY+cG/VCTer6y\nagY9Dl0475LushbdnQIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICWwIBAAKBgQCcbT6fcGVkx/r6Hx3UR8nP2CEtR51f3IFmHxdOpEa4tkYU91FI\nCjhhyxITTu61ZVCDBJfFyLu1XlXPtAYRehIJBJdCZJhIQyeruEVPzEUn0Igiaz1Y\nyCATXPeui5U7LLQDUm4NImHgNYRjY+cG/VCTer6yagY9Dl0475LushbdnQIDAQAB\nAoGAVkIblToaf2+TY1fDUCriC33oFZr3GkRzCog8hv4pjXPdw3P521rfanXbmtAc\n6+RZeFYRB1zAvauucCGacwq4ZGmZu4Ghh53G/62Qya32PAaNeX6dS3XUtGz7phr0\nHL0PuFs8yyPtMvA5fPc21GbHpQ2bYXFbq/b00BdBbyrjA2ECQQC9JImn0PmzSIYK\nsTSI0yjwBK+khpbM8cVIG9QMafH/dBW6cnJb/LMI/sIhpkT0cbHcTCoQ+Kncp/DT\npN7zvO+VAkEA07g/e2xrpU9Sh0X6XHVqyuIZ6OpwuPQhoEJ0PQiXflsDcLdrtJPA\nzbW90MeXzAVTeXPy8jXO9mW7EFnxtMXT6QJAHgm3ctdVUIur/fa2iSQ/1B5qZo6Z\nVGLxGcqRmocYz6D38mxKjSFMrZkH66AkQ03rGTlfVOKo10o0jOgaIEtZIQJAKLvd\nMuDkQRTm2vHivmE0373qoD5i26LUyWGfvZJmmz/lhI01orN+t9VMpNuR4AXyTn65\nclJZ9FwURowXjeE16QJAQdagMnp2iV0OsiJzQZPrWX8GXnl6yLywKeGd29qcb9mn\nmUojYjMCRSgNPFsn85j3wlmeDOJWhxZwGD6r2t8frQ==\n-----END RSA PRIVATE KEY-----', max_length=2000, blank=True),
        ),
    ]
