# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0006_auto_20151207_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCmULhfcGHMj2j9i9foEIL56Exp\nWJoNSyJYM7qrOOfLGeVsX2zN5ASa+lKEKGJkncYHvZ7NO891IpKxs8Zue1azf6tE\nKD1+dvKdViEKk3K+dSnGAUPf4yeA4zzykQx79gicAn6Gn2SbUuPPe9gT4dBdkId+\nyPp0tSJ1WWAV4+rpmQIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICWwIBAAKBgQCmULhfcGHMj2j9i9foEIL56ExpWJoNSyJYM7qrOOfLGeVsX2zN\n5ASa+lKEKGJkncYHvZ7NO891IpKxs8Zue1azf6tEKD1+dvKdViEKk3K+dSnGAUPf\n4yeA4zzykQx79gicAn6Gn2SbUuPPe9gT4dBdkId+yPp0tSJ1WWAV4+rpmQIDAQAB\nAoGAKw7E3PiUaUhLjzDQQeVcc2S/u5pTr9Ne3eTuk/uUjxFyQx9lZNx+kLzz9gEa\nkCAEr+ZYoZu1dwbvYZBAdEP8SuuM8p+vZWkuKsaBfI30FIAPuAMfmxfmSeYe7zF+\nUbb/1V3e2zBexQvjWr6mvN2ruvDY5Q8oP8auiLHsUYe28P0CQQDLNnfAoNFUskTY\nXNfJ9mNGuukbANdkSyBhYmvFWjgbK+j9XLHBpYXPlL5wf0x79vo1nrHU02zW989Z\nI5VH4aSbAkEA0YSX1AURywDPb5CFTBvr1DfKSHnj6hI6wCeq1bEpFXTAc/NzIxeN\n77IgJb5juDilLQOJw/yPBzd3uAJkJyBb2wJARLJeG12CRpqZUXdZb6n+d6u6H+nR\n5tLK2IEYI7hTHURj2Drc0LTvHnSPSKKQLZwZi8ThIyxyL93IV78CuTEbnwJAEwPx\ns7ByGPaN3RZEws+V68DUfxdw9AGLi30OKC7YB7Z88QkbXgf5PdPwzvwkmMerVhaI\nHl2Bran/F5g/9r0dGQJAdO6hTb4OmpKSTb9GWTVVx0nEtxF7l4wuqNbKkcHo3T6T\nQfew/NuUg+mpLgeo/GqMrtcPjksWcINUkzDsl9gmYA==\n-----END RSA PRIVATE KEY-----', blank=True, max_length=2000),
        ),
    ]
