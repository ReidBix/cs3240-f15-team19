# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0007_auto_20151207_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDC3riLluPUhj/n1w7tJ4C+9WOA\nqvPrPFO/sammXD0RcvDHueek5INHnOprt5+rFEhep5iJ0F1lb/jkDLi7IEHLORaZ\nz179b0s/I2NGlu2N+u8kGyQON0kZUMucrtkJ/M3AC82Vxu6CYXwRcc4aKbwBHJ54\nF0ahCnQLnhk20qnVNwIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(blank=True, default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQDC3riLluPUhj/n1w7tJ4C+9WOAqvPrPFO/sammXD0RcvDHueek\n5INHnOprt5+rFEhep5iJ0F1lb/jkDLi7IEHLORaZz179b0s/I2NGlu2N+u8kGyQO\nN0kZUMucrtkJ/M3AC82Vxu6CYXwRcc4aKbwBHJ54F0ahCnQLnhk20qnVNwIDAQAB\nAoGBAK+wOVWwjmu3NbqCC/UIXmzLtA/3EL6OvzrepINWOcCXjjmjhBMH6swPztGa\n1ZtaR/z+wOnPL8UadJy2U35yEJ3jdkz+Kx4tahkeVYOmz9ISg/OnGO+LvPuZEdgT\nvl5nn6IrZTSRku1LCgQXLuOyZxS7QzxArHWn+aUlwJqYSO3BAkEA3yECsy2KFwiq\nEJ0SQUevIAe5tcKpauWWznz5uMdBZ67sUA5d2UxXt23PEQuGarFqO9El/QyNeXut\n9blRCaluZwJBAN+T9vJbQCo8v4yHMudDNAQ8zZecYDqVX33+h3w3MO41ZHu9I5Hr\n9y8FBGO+0ARIXkiI75zWHJf7xDbt2gOHgLECQA8BEkRoQIvx+jWpykt3fZBC1Lsj\nPu9ARxbVkplZVM2bFqr/fFIbbx6XlMAJrV1JVuJ02wAcMvtDVNxcPNXQfesCQQDE\n/8luDv1guhpFprMxlsN0oGa/GiioNgnoKKgUyUSyABXD+gonf3VT1uXhRbZgr6tz\n2kTXOsoDGPHxPG8HARRhAkBFl53kn9dVdbkvyyREJX7SGMyUcUa6qkY718UwxxC7\n0u0cZoNgJtilSQ3b10/bRZtONoNurxBacH06cbQIQEav\n-----END RSA PRIVATE KEY-----', max_length=2000),
        ),
    ]
