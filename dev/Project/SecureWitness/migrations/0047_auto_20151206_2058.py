# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0046_auto_20151206_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(max_length=2000, default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCpEFfO/k1Ywgu/VLuu8I4h32nM\n9T6gjM3gOjZObQEQje6vQoMI+KWu8+3g7tAYbMfOGDPTxsUyACKtZ0RDPtTkNOY7\nLSE1RqChzBe8eeI9LT7DyyuXaRU0Mk9r0u+/4BhTPaZmsGoPf+ODpF1IpcZu5p7E\nw3ki+zl5g/QZrsCCDQIDAQAB\n-----END PUBLIC KEY-----'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQCpEFfO/k1Ywgu/VLuu8I4h32nM9T6gjM3gOjZObQEQje6vQoMI\n+KWu8+3g7tAYbMfOGDPTxsUyACKtZ0RDPtTkNOY7LSE1RqChzBe8eeI9LT7DyyuX\naRU0Mk9r0u+/4BhTPaZmsGoPf+ODpF1IpcZu5p7Ew3ki+zl5g/QZrsCCDQIDAQAB\nAoGAZ0o825Iy309ure6u3CrMK5W7piUPpjdgcOYf17pxNBQDB8CzHgAL+d++Lfa5\n3LJZQGk5AOIoCGxcw2ScKBlzJxsC0uGGgcNCPEQNX/zQtrpZE1XssLxnZgR9AYlS\nJuY496kjDIjGPgeAQL2g4leofPA2b8qES5ejoNIA9iWaH2ECQQDCiY0eXAal041p\n6srRQE+vb+WoG+mALh5kM0NgIhn+y10S8zKm7J0/UkwEcEIpjy+k95lK1IasJCt+\n4lzNqSaTAkEA3np2RxOFapvgob47Zr+SRgGFF9wHDiNfyutf5410aq/yufNb24pl\nBOM1FLA1pBgEVBieMSl0y/5jG7eCoUF43wJBALe9y7g9G1pM8mh0B5SUta7ydWvO\n0UDsTnA9qwmFrB/oXMSlR9Y57lv8kyguD4/JWirqYbM4AOteTmbNzvHBLlkCQQCD\nnakpZUgRiMP8i+DyaTTsy2tkcRuPZqf+EP88qjeMAikzjt/x4k7e9FdrtM8XE8pD\nwgicBu183TLeq9LQ+T27AkAcG4RGftk6EbixxkgdaFcVPfRiF/vNHiu5EJO65abz\nD9OceqiHZvDMjtkHhN66P/bSNUnz4QFGnruX3dnbz0T9\n-----END RSA PRIVATE KEY-----', max_length=2000, blank=True),
        ),
    ]
