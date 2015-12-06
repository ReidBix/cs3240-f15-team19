# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0040_auto_20151206_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(max_length=2000, default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC+N0bVIehy9yFbu37BFz3pQ1v2\nt5L2F+n8oF5c5awIebTqnkx16YTJ75uczBH1p65SdnPw7Uu1MmHFhffneNMry6mV\n1EFFcRo8wOfSSLlgzznip3uVpmKt2Wxa/1GGE7BU2pzLHXIp0HTNiYPotXoYGDTb\n+AFJgUtT5uIDpJiLSwIDAQAB\n-----END PUBLIC KEY-----'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(max_length=2000, default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQC+N0bVIehy9yFbu37BFz3pQ1v2t5L2F+n8oF5c5awIebTqnkx1\n6YTJ75uczBH1p65SdnPw7Uu1MmHFhffneNMry6mV1EFFcRo8wOfSSLlgzznip3uV\npmKt2Wxa/1GGE7BU2pzLHXIp0HTNiYPotXoYGDTb+AFJgUtT5uIDpJiLSwIDAQAB\nAoGBAJD0oPcVAwZxjCtS5BKT+qtDmNaYKNd/e+H3+FFE+WfwD83n2o7U6UvWXDkO\nTvVs1myjNlG5FEO+ZEHZiQUNz6Yy8igsgK30NhUr8i5gvbdPkiRe2aonLGbwvXyL\nt48X1/dzbyFhx51yOITX3IuHGOsAdm22BGziQiXQjyp5C3gRAkEAxSKd0NXz7HaV\nDBGYuv4apuWluv4dbz+IFEbKXsMGK22kiOM20y+1TqBvEvlHrYGs8hFkfvKkEjep\nVRH8y/dJuQJBAPcDvIEJ/JAdqJFAW98eg+bn1PIzO2NIiOx3A1zuTCjplv7aOLjz\nwxJg52cz+DKr55JeV1twe9Q8NMoZfsuEryMCQCrhzNKQt+7IHMPzT/XdMI79hX+X\np297sm42t+7FHaJ0x0W/pz1pM1dXLtJBx4XGn4hIoEO9JFOSKBOJRiRYNoECQQCn\nR5J62KZ/enZTl4AgA2xUDR/6vZM0U0TWzmoqnv5YnogxIttS9VFfutw62cj1l9EF\nIHqMZAqX2gXt74IclUh9AkAi756EuM26rilpvU+UuNQSRtKdJ0DMM9jyUWTEcgmX\nl2XR6OOvsw+do4bwMl3pBxMHetgKZyF/gvEYt9JpAhrk\n-----END RSA PRIVATE KEY-----', blank=True),
        ),
    ]
