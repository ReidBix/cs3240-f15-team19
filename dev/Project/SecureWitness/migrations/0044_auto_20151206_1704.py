# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0043_auto_20151206_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(max_length=2000, default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC3l70IAVk8wnEJjRg47YktesMg\nrDYYkFfG1+u4036aIT863tfCJ1eR00FgK4nTjOEL7GhHAkEK8qlzJSgNIVK4Dadq\naZXflmVz60w/39PBowKPjwOQ8jyMGDbLrd22t3pNPSyPricoqKeWDlfI53uOJTk0\nee6R8dvDUZeprKXccwIDAQAB\n-----END PUBLIC KEY-----'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(blank=True, max_length=2000, default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXgIBAAKBgQC3l70IAVk8wnEJjRg47YktesMgrDYYkFfG1+u4036aIT863tfC\nJ1eR00FgK4nTjOEL7GhHAkEK8qlzJSgNIVK4DadqaZXflmVz60w/39PBowKPjwOQ\n8jyMGDbLrd22t3pNPSyPricoqKeWDlfI53uOJTk0ee6R8dvDUZeprKXccwIDAQAB\nAoGBAIjuM5704onevFBTW+2ZvOae2UpVJ0PK5Kz5/mYr2BE9GtvduS6mCTpKRkhk\nMLgIKxGpkVzk4X443wlyfRzN7dL1czLGt//atsUJt5VD9ayL8EJ4jxKi8JG5/eg2\ntpUA9jvEndErxDe3pgR0HN5gz18w/opw7F917x+ApePH4R4BAkEA1oVP+6enOHT1\na6NhNEQ26ac/ee1wEWYiQIsVrCv7QRH883X0Fx6hJBuRivaNBiXO+aX99+uUDTgj\nHPMVx3mUQwJBANsXgHE52sBdxEyPpvftI/r8i/N5yc12sVmO34u23cehu1Lhe0cl\ngUEvnCIALxJIwhnn3zGyy8U5AeoJBvXSrBECQAJerqeFDp/dCukJgQVmy4SBSH48\nVUSb8DzuTGr+gWQSosy9vNiUigswEseKObybplGzt76JZ7VNrXWgadkuSqkCQQC2\njXORZIJ4DOk2Xe/i3u4/AFVgbxcOIxsNI3XyxVEwOPuLyKNemcqEVTZEQmD2XDeX\nPFQF5hPR5nlI13K8O2jxAkEAtlg+f9y3Kervv7j04JHFJagQqOInorqrcxDXarMd\nGjPcdh/LVIn9i+PFUwNbbUFW5P0ECbBuv24H5NNYCb7h1w==\n-----END RSA PRIVATE KEY-----'),
        ),
    ]
