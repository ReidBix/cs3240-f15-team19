# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0032_auto_20151130_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDiuoWHEmkifh0RVsmTpMVqU4IT\nBwcDLBc8IZ+HsXnTpxgyV2sjuvuMZVtiuirZ4Ah/00zctS82H2W8SBKd5SAeMIAB\nA4WFC4Bmb46XUA2K58mLfBp6J1+I8oO+1AX9vLe9UGsvdGaVKFMOd0jP+N6b8z3K\nj9WcHYHlNo0cM7t8AwIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQDiuoWHEmkifh0RVsmTpMVqU4ITBwcDLBc8IZ+HsXnTpxgyV2sj\nuvuMZVtiuirZ4Ah/00zctS82H2W8SBKd5SAeMIABA4WFC4Bmb46XUA2K58mLfBp6\nJ1+I8oO+1AX9vLe9UGsvdGaVKFMOd0jP+N6b8z3Kj9WcHYHlNo0cM7t8AwIDAQAB\nAoGAUlc9ES3tgrpcYiSrtnQbwh6r2a8uq8dCdPMdFdGtleFUV0wKPAK3Qmi5BKTp\n1RCY5ZteibU/fR9v+i4OnMtOmxjhbO6t3tr7nZ/kj/T6dM0kE8oE7+X/CWQp6gfZ\n9C/4eIDJzNKQQUZqLICFupXqDi/M7d85boOEdGxxh/QN1ukCQQDi43Wml2BxCYCP\nFY67iuNIWZ69nsgW2eq/N2BHtgqSOQx1Dy7PD07D+qBCgNSsCX9OUBu+mIPGfbge\nuqDAfdqPAkEA/9HPMvPIt7yfIVFbVy/TixPjQaHY8pmQ3ymrOqSvHVKY9yCy7lGL\nOOMQRJF7B5nV1wypyu61kclf4h5ki27RTQJAXN8SZ3CLL3neP7NpS2cchZ75lVCL\nQp9MsZyvMmtXhGcJrFjcpjDz4tCSDObDJvB0RdAQq0Gunu8TELD/4AskDQJAN9my\nhsk6dQK1Kyz76BkE8kQxRU70cmKcglwyiecSZDB4PNvitK0Q3CaWkqHAXnRzfzPA\njhF3ipCQYmmIQfi7sQJBAMCXoNANbpKFCevlFar5JSmuM01s9SibedI+7EjCeFY3\nQkPAWnXc0C+XxKjbA4AdePmlqhOY6gZSIdtqvTXsRfE=\n-----END RSA PRIVATE KEY-----', max_length=2000, blank=True),
        ),
    ]
