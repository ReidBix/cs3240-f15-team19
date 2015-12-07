# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0049_auto_20151206_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(max_length=2000, default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC5r50lSWvgGeOOL7ZEriEtvLT5\nbWzSgOw28gy0GOVJdCnyce6NZRpBc/eNBR9I9QtEr3T2WGY+UnwgbtTx3lWr7LZt\nodgJS1U/lDV7EqHUI85fVU9NNT3tb42+/U5oIWQEyg4+1VH6lB3AAuoMV8hb3kit\nggWVc0930rFGcSm8SwIDAQAB\n-----END PUBLIC KEY-----'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(max_length=2000, blank=True, default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQC5r50lSWvgGeOOL7ZEriEtvLT5bWzSgOw28gy0GOVJdCnyce6N\nZRpBc/eNBR9I9QtEr3T2WGY+UnwgbtTx3lWr7LZtodgJS1U/lDV7EqHUI85fVU9N\nNT3tb42+/U5oIWQEyg4+1VH6lB3AAuoMV8hb3kitggWVc0930rFGcSm8SwIDAQAB\nAoGBAIuLsummt+9/BUiCCtSqmDyrKMaaucGpKdxRI8LlQstlBXEytjiE1qqB4HSW\neOB3Z7SCt7+6x3vmuWoWYOo0UOTPIX0iejl1vjbfRxzWgcDZ7qvqxUrogvc4twc4\nxa5NupAQFjst1DkwFsqXq2k5Dg7+T5/MIQXkSGLIXVnMYyABAkEAyfGQEu4U/ryp\nHqaiLJAVHeLw9KAnHwsu6BAngafglcsxKD4JsYJQXfZYB9JzXGO8F4CXHURRUajO\nTOUr4cFUAQJBAOtj+lVOJYhUk7pTDTiom/iYVzAsIsAyXxRL7BqClioacxCTdcIT\nXZhO+nYve1o0M5lMSWUv8nUdfOFhjysGIEsCQQCvGtodv/nOhNJ0dHLtByZ4Wr8q\nrvAdN/o9WTyYbXQNDzqZtWl8VQ3Q2/mrFq3XL9f53ROrWgDVOPVhsdniEFwBAkBm\njet+CQsPJ5IpRo/nFIbHu0+ZPFFznT6RcDaQoj5cX6OsICLZCGjpt9clcLB0b3Pf\noT4E6OvgnJVQ+JlQrF2bAkBUlv3wNsDJlgX2b7PG/rehN0NQQAA558vHzUPy8oUA\npkiaVt4MbfB9B+5BNCYt4mLV+bZF4pdU5qP7RCZvlQ3q\n-----END RSA PRIVATE KEY-----'),
        ),
    ]
