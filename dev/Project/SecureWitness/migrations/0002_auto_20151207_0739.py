# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('SecureWitness', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='rKey',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='uKey',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
        migrations.AddField(
            model_name='report',
            name='group',
            field=models.ForeignKey(blank=True, null=True, to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='upload',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='upload',
            name='name',
            field=models.CharField(blank=True, null=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCu1bDNdyTDpZ8WOiYVtnPFC7F6\nZEdwR7Tw20ZML/d04TmfjfC2wtBOWCK/DdXA+4vhhtJIJGH3xFXqwS75WtkaTMWZ\nj2fPQBPfOsiSU2dsTkzAwI4jOig35MnQnzMguZz6w3ZbWDYQzlrzxZr4Ki4gYeJJ\n6unAPnsT4rNx755iIQIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(blank=True, default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQCu1bDNdyTDpZ8WOiYVtnPFC7F6ZEdwR7Tw20ZML/d04TmfjfC2\nwtBOWCK/DdXA+4vhhtJIJGH3xFXqwS75WtkaTMWZj2fPQBPfOsiSU2dsTkzAwI4j\nOig35MnQnzMguZz6w3ZbWDYQzlrzxZr4Ki4gYeJJ6unAPnsT4rNx755iIQIDAQAB\nAoGBAIAZTeudSjCXXxKYFGOARR6wzJ7Sbo1T3L1EzCLyWisnAmNnSmF+J8XfScYW\nSvGU3Q6nC9eT4Lv6/MB+Pv6wk7Q8DXScIKOCRFzSqc44BQkp+P9u3BcbkTXdAjg9\nqkDcp6BMmeYbj4rzqUZwd7+Rd+epfAlE/PilEQSkQqQxTu9pAkEAwQfSXboONJ3g\npFUddaP0lX+ZKSV+TNSK0xpYo8aEYA+jGmJ2JrCqT/Caly7eHDrqjl3mK7F9EVxh\nCrzXF1mFCwJBAOfeUSkZar85ON1HnhmIIl9csCCuuC+HmHpyGS5TQIoWAuxLS3OJ\nGPr/MCGlu7nd9tWeiohDWoGHA1cGAo+TWQMCQGgGRRIJkFo+sq8cx3F8V/Sw/OM1\nt2jEKcQ2MIqiEviJtMYlRbL4BfBqo4TR1xSzk3ABnmbxkYrnk8xrlCabMZ0CQB1a\nxvmmDx6gdvOEwp5G3tsl1+J7XDQgPYya71cvEQeqW7pgme/JlpEIR6aq3cZdNIe8\n55rys/2cAy88Qoy8wdMCQQC4xqzKAYudQ40BM+/y3SdnFKPW2Eq9HfFxaNNQevwE\noFO97o2xQKeAl5kW7k6YDHUgCplxcfB6e2tu9pmRtscF\n-----END RSA PRIVATE KEY-----', max_length=2000),
        ),
    ]
