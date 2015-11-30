# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0035_auto_20151130_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(max_length=2000, default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDDYHRhAmlDPEmAHzP/YbaHjpRD\n8wEKe/moEqsU5+ZOo7ea29FF6ivLcYfWw5b8n9qEkLkGxy1eOhNBy+Jlbu930EVm\nQpaqsAcLEoNioyu84tmzMm/cdikMAlVM9AJKbJv0QSCknXKSkJCHoKpZoojXaIXg\nfBN+6bU6/NlcWUm/8wIDAQAB\n-----END PUBLIC KEY-----'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(max_length=2000, blank=True, default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQDDYHRhAmlDPEmAHzP/YbaHjpRD8wEKe/moEqsU5+ZOo7ea29FF\n6ivLcYfWw5b8n9qEkLkGxy1eOhNBy+Jlbu930EVmQpaqsAcLEoNioyu84tmzMm/c\ndikMAlVM9AJKbJv0QSCknXKSkJCHoKpZoojXaIXgfBN+6bU6/NlcWUm/8wIDAQAB\nAoGAE+e+06dgPBZnUqNbM9irtRHkryuR3pSU8fe88GtT/o0VhrSAlMPv5FFTyqCw\nwFo09C6eez9Nsvztu1VfYoAz625t915ArYfBTlBaBx/Iz6Q5ZveljH4nM6ZHKk01\nqMCPgoGHbbOvSqxeTDqIQ/Ct8FaMayGGuj5iMXAygZ8nl8ECQQDUYZBD+gNODCuO\n/rN+4zlZi/LLFEGtzfTgLNDUFqqIOZuJ6hf2F+rI6rI96ZQwZVUSLVpb/lRyGrgL\nsYetrhVhAkEA64DZKx+iMK4mpgzQMtEa3X940ezBtbIXun4J7p2t/jc1+kX0F52V\nlMVdbLPe5/bD17daOjyDGzlwo3rOgrDB0wJAW+Qqy36tV2OkpSZG+6vM8JXA42VM\nVas7PJOnd1ynRHHIfo+u9me6ylvh6y/ZUmdFu6ur4QnV99jfsQ+LKPadgQJBAJ+q\n1xJOuzcIC7oO++VIMk+0SiUBwP/ARCgzpeY6z6mIozcQ0IJmW/DmswWtGdbpTjRl\n4m2Tc0w08HJWI8clsfMCQASWwTfkCZ3N0FDHz5EtRwsDvdf3Zevx5atnb8PSX0vg\nd00kbuSWzfttnRGgPOslJy9toH8gIrU8yrW+OqYmaUY=\n-----END RSA PRIVATE KEY-----'),
        ),
    ]
