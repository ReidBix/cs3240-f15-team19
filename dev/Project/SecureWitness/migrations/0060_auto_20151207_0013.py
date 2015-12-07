# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0059_auto_20151206_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(max_length=2000, default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCygXmT3Xil1Xl0EHexAQxC1BwU\nWeucpnrJrElY7znS7olhFdtvMNmbEDrbHobRGV8YQv7q9oWQ/hXXQbo/zfncuZx8\nCq8VOAs7ap4GOsiej7QJXcJ9rSYMN+PirCvOQ3PMsz1RDrF9ev0ATqZOISwSUztm\nHoshIcMauBp3QbiBMQIDAQAB\n-----END PUBLIC KEY-----'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(max_length=2000, default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICWwIBAAKBgQCygXmT3Xil1Xl0EHexAQxC1BwUWeucpnrJrElY7znS7olhFdtv\nMNmbEDrbHobRGV8YQv7q9oWQ/hXXQbo/zfncuZx8Cq8VOAs7ap4GOsiej7QJXcJ9\nrSYMN+PirCvOQ3PMsz1RDrF9ev0ATqZOISwSUztmHoshIcMauBp3QbiBMQIDAQAB\nAoGADBMH90GG1KjQ81Hd1sI8YxTX5WSDtG/qZFPcDkD4R1VNQ5zn3+iM/5kkcgfp\nlKFDtm9psNkGBd25+np+r6wuF2wnPu6iDITermjy2Igo2MBNKyu6MV2tyDuifx0I\neJ9NOXxKgchgqAkWvFbHddGapTHTjuIK2EwBUoF7b5vKbzUCQQDVe6nHA3xezzEP\nCPlZYcxKoAC18bXVWFb8U5qqXV6RrMatCUFPx70YsnlKPxvLnKYH18T3GGCNEBXH\n/bdLGpcrAkEA1g6Ck//1ijkFeHEaVeqqtBNt1lcKfg2y10UMnF2sSTQQvFfch4G4\n5C5hC+wKtwNk4Bs6uyCdMIb8OqtTf4lbEwJAXeb+P97FpwJl5uIgo/NDpBOLHHzM\naaJo6KZxorxdK6Ce51/pzYjjIWjntwPZWw91bH+5UKL1XTcVDZoJNMzmbwJAD2Zt\n2I4CsVYW4appdaLzcw8uyMvsUlNT+Y7bMGjA22dmiNZdZFZd4fTAQKZTwwT4ffMX\nj5zyEiqz/NiUoklUhwJAWYf1KrKgmeMgUCSAmR0L9GJ4qlIW+lyr4harzTaEg3ra\nBUNkEERA9SjF8KeN1rZBOe7buNxI0bMfQVf5Nf7rFg==\n-----END RSA PRIVATE KEY-----', blank=True),
        ),
    ]
