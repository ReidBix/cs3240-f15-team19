# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0028_auto_20151123_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC35aKFBio9Hm6pctnE+WjSPbE1\nUNBpd3txJutsyGmd12sDnKEqz8/MV98v5DmXXvsVOh7HXlhhkh/DynRI08fktqUU\nXZIEtFNHQHRKBCXFtRpUGllF/JxZg5mpCqukZTqiXn3EiMS2aaM77uf7lMWY4mmX\nJYwzflORV0jCLORvPwIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQC35aKFBio9Hm6pctnE+WjSPbE1UNBpd3txJutsyGmd12sDnKEq\nz8/MV98v5DmXXvsVOh7HXlhhkh/DynRI08fktqUUXZIEtFNHQHRKBCXFtRpUGllF\n/JxZg5mpCqukZTqiXn3EiMS2aaM77uf7lMWY4mmXJYwzflORV0jCLORvPwIDAQAB\nAoGAHj7zowNnkRPfSZltPdtzpRime8ll7eLL98lZ8VNpI5/Zpwds7pitacOOHtdf\nrYjerRgZFdtrl+irts0moQ/MEYdq/PAN4Np9uYFfmovewAWG1vv/8VkM7ErtTgaF\nC/7/hPnF5LZRuIO6FtGkASKBh1TqCkYc81sjCyD5odtWBgkCQQDIUyQE5RrIlAgf\noslQn6WUPxhYDzfItPonwpisp3ICv3ML1KDElAF01QuOE6EWUk0UShjqUwuiBJdm\nTxAWADxdAkEA6wGt9ubLXqi1Qf6O5HckU1QDYWpMsFjFIWzIyg2Kwcb4qt7yB3CM\n7VVoaR9WU1oyQ3Zdnn4RFRXBrWmiAvHASwJBAKiwMk2Y63PqC+kv+FxXA2SRuRs2\nPWBa3agrmssQ+dXMh8F3nKXMiGlsmZ1bdDPKvDOQrehsZAhb224At+f+7NUCQADA\nxp/t6WTqQXpuqGKPByzFLiWXw5slDaynvpT3KiSo0I8rm7buY2U3SthbY1ltBpA0\nxuQFH2Tj5vT5S62avLUCQE1f5RXRFBEPmgw7DBZTb8zricIj/IbbxTsqFjoH4r+a\n2UGv9sEKowCQQ2E9V8EYNwdeFbBjfYQnUaGw6ZES6GU=\n-----END RSA PRIVATE KEY-----', max_length=2000),
        ),
    ]
