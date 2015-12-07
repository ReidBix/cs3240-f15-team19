# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0038_auto_20151202_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC8eTywPAkqW3m/XEOP+dNGBJQ5\nxATN1sUPHLTLHB27eIYQpFCWhMyHi1tG8Ov7m180OJwRQNljpfcFERq4UrXiunqv\nkGh2W84GHDHvL/HCV1cyMQKaojVOVEyv+y+LDFYI+cf5zoRqmg/UvXZctsBlx1Ci\nTOW7z552FsRKOKhhpQIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQC8eTywPAkqW3m/XEOP+dNGBJQ5xATN1sUPHLTLHB27eIYQpFCW\nhMyHi1tG8Ov7m180OJwRQNljpfcFERq4UrXiunqvkGh2W84GHDHvL/HCV1cyMQKa\nojVOVEyv+y+LDFYI+cf5zoRqmg/UvXZctsBlx1CiTOW7z552FsRKOKhhpQIDAQAB\nAoGAEt2P1ZQs1rCRXzY9DQxUuY17yMx2LqRw1TJqZmpKD5ng0YmhB3ADiQ3J9S/o\nbyb+QJvqA1Aacn8KWtd7dTfSPNNklAtPyggdl1i68MCon2Lz5NWc8Q8CwiDVLtVN\nPUkU6KCdJh0QrQFbRnVML3nxNlxiN8LjT4IB7Ov/OxEpTAECQQDDBy37uq34F9M7\naNmaqCcK2ncOy9UsHLTE7YHZ21k62SnK+dCBCkVLMI67XQq+VAaK3J0EJ4ZJxtrH\no+8MJ0mJAkEA92V6t36+txUghijezv1t5BYG8DGEDuw5Q4kHAkM8L69hdwJY+2rE\ncsN+zivdmD2H6lLEJfgvEkYqYCKT+mH8PQJANwwVvJGqfPYslv43PWHs8zFKnZCG\n8NaBZ3wqRJWXD/cvxqzQXzvI5zojb1sJp0MMPbGbWArX6ocIRYVN+b41EQJBANF+\nFVSc91KBiXER2trcr9mc7XMn+vPIBRWzS0QXOzgGAzqLul3sIz4rXY2oh5ULRbSf\nMYoVh4ap8+hEX5p+ruECQQCPKXMfJT3Z+p3WsiPNSGUuNSIiGyFhyu0oM0CpRT8R\nMT3qw7mGKEmxpXlbKFx4Y/E1/YSl0RUgyVIsclOhANHH\n-----END RSA PRIVATE KEY-----', blank=True, max_length=2000),
        ),
    ]
