# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0015_auto_20151207_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='folder',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(max_length=2000, default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCh1sd+lITw+k1YjjXY2m5HZupJ\noM2A9BH73U5ay4jMGDhIsJQ+9iEqec8em4xZH4o+CHisNN8AuDUbMncJvWIxG2Ij\ntouTKGH9rRQwVN1yQDMFHcE/BEyWu7O+YM/l7HztPHgz+nkdeGjQeX58iyIpsz5t\n6Ad/OhYQo2IfN2f+0wIDAQAB\n-----END PUBLIC KEY-----'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(max_length=2000, default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICWwIBAAKBgQCh1sd+lITw+k1YjjXY2m5HZupJoM2A9BH73U5ay4jMGDhIsJQ+\n9iEqec8em4xZH4o+CHisNN8AuDUbMncJvWIxG2IjtouTKGH9rRQwVN1yQDMFHcE/\nBEyWu7O+YM/l7HztPHgz+nkdeGjQeX58iyIpsz5t6Ad/OhYQo2IfN2f+0wIDAQAB\nAoGAR/veVAD/eKf8iy0F6mSNtJikEQfDIF5vOVXgKiZpvE3xivNvnOmhKuFvLLAH\nJwUOWjUuZ3pEzm8gv+4cYGqqJ3RxJomQmVC6Uh0ICuc9PhXJ7flqAMawFKqJPkCe\n/iH3jPcCexedRlr/W3zjKmIsLhqXacs5IseIRXBqX4QdZbECQQDKHiZdrmgIC7yl\n7JOGoQSOUC1DJDZDqQ2vNfublZqzm9MNmRqRBZHsDaF7yJNoGHPbdKJNS0s4b7Ho\nFDK+uuJ/AkEAzPu9LanNerDlZouSV/TlGwsnxwMHTmAYEdTj99rOvENiUJmPq/JX\nm7E+lgXMtL8hOXM8Jql2RVDkvczYF62RrQJAMc0D/wk+MN1Tej60ivOZv8cZn/WI\nOVuqN4XBnTBbke3PLwaOeTU6I0Ooimt9hqSfx28RnqHywtEisOBpMH2z2QJAPAmD\neCtitou3NNiuTTq6G7ihtuVJL4hvpFFhT8fzgyqNUiQX83mwdTZtqU0bjtjoJ0Z8\nGKrLrDOsO3cS16SLpQJATPRIY9icm9ZZQcdBU1UXTxIn5pOydyypDE9geJY3/XWI\nbIrKanMB5Ky69+Ekq9dop09TZT0UoocUKMaKtM3Xbw==\n-----END RSA PRIVATE KEY-----', blank=True),
        ),
    ]
