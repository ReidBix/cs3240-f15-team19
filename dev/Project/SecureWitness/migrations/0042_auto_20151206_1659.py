# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0041_auto_20151206_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCl8y9rg1D6HkMg+iTTDY+49jl7\n0Osnyq7GNiWdArk2HR6soaEgO+6kEEbYRDh9cAqNJZ88z7iuZOpx895qEidpZYuV\nCG9FaYz64ue5r/DQxt5EOm0/iZ9EQLhjhANwEE5rSkMBm2VNr6ldyxrhxbSrn4NR\n4rPj/GgSCpIQer93awIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQCl8y9rg1D6HkMg+iTTDY+49jl70Osnyq7GNiWdArk2HR6soaEg\nO+6kEEbYRDh9cAqNJZ88z7iuZOpx895qEidpZYuVCG9FaYz64ue5r/DQxt5EOm0/\niZ9EQLhjhANwEE5rSkMBm2VNr6ldyxrhxbSrn4NR4rPj/GgSCpIQer93awIDAQAB\nAoGAatq+wvSoNJU91kMbaQaHb6qj8vTgJhwdE6YT7Biv14dClBfy3wWYMO4GIAU1\ndpepQ59g/FAoc6qpRzynDxenZe1FDwU9gvwfjPokUExh3hm+ldeSfpTdDeHPQprM\nHPQ9MF1U6WoPfY5khOWVXdo62CvfOzDc5LqJwPbdaL5RCnECQQDCRiv63Y5n03vq\nMINM5T4/iOx/i5abmH9x/RwRU0/8cnTqIjcwyQoHDB47bABP2FPovHIH5OFm+45o\njDQ0i1UTAkEA2q0wKNvv425sKUUnU1zAU7QOKSHFCJ/JF2CA7XzYw4grFxX4N/lV\nLF86j9VME05okxEohMRcHELMRPRcaZKXSQJBALsizxCKxLccj1uKOaAjnq+i3HUL\n6BqfbfxGXPgPcZfyRM6YAOPcc+1P7fs9UJuY/VLN22XhQoJpxMbObydCI8MCQQCh\nbqsX7s2YS0ND8E5IxzcgU9MEYG6xoCv2uwJS0BDBwHt3Dnvw7nsHR8HWvvLrab3f\nnBIaeU86ecGMwgyaz2IpAkB9iUiQoznmTBMSWJRwA3idZ2VwRuEIj9uA9AeUhXcs\n4FhomBJdjZgiUGI71aPs0dPn1zkoGFqIsFIHzL5doNcq\n-----END RSA PRIVATE KEY-----', max_length=2000, blank=True),
        ),
    ]
