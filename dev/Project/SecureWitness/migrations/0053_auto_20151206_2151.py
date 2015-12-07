# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0052_auto_20151206_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDa9lhlhdp5CjVZ7oYGrdKV35HN\ncdccaYyYyXu4pjD2z98/vZbMLl3C37EtxTwLeYVXy9hEg8Or7r+hpBEFSLHC1Yng\nc1hnB+TpqZo2iYI8GZVkV7IZWd2NXMCwhXA/A4nOAPH91tkL6Hyc29HmcLk1ASPI\n7IxpjS5e6DdlxFalnQIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICWwIBAAKBgQDa9lhlhdp5CjVZ7oYGrdKV35HNcdccaYyYyXu4pjD2z98/vZbM\nLl3C37EtxTwLeYVXy9hEg8Or7r+hpBEFSLHC1Yngc1hnB+TpqZo2iYI8GZVkV7IZ\nWd2NXMCwhXA/A4nOAPH91tkL6Hyc29HmcLk1ASPI7IxpjS5e6DdlxFalnQIDAQAB\nAoGAGO8qm80FVvlBoA8YdhQ/Qc/mw5VuII8ocpGnJBzQwJplWtXVIUU6aiGdBJBM\nSSY6eAf/hbXXh3G1osuTIJ3pmAc7fKI+Xs9z/MlZbiqXLsek+mlAqICkkbjkfWPP\nlpAqLv/8A4e0Ivlh4wfxwfXFKCFkEjCAzQ/30iPHN2GQTsUCQQDdSVUPI2s9zG4+\n23xbf7rAa8Zlr9Lu7VcL9sLV0YL+m7+0g4QjNIWvSPesXwvF91YSGm/pErw0UJNp\n5BCe1f13AkEA/U+tME6bD/FM5CJkj1Btj8fRh0qPGDK2Wefu+qzAWZAhOlG/GwH5\nvJXW3HpepSl3zSxIOE0znYKDGDHQRBOqiwJAW+idX5BCdoR2Nb1LxWUj18/rs0h3\nv6zsPpfbDJvcYIun7/2/4C9sZwVTeVBwv2SfZx175b5WVRQyZgTHsnEGuQJABuBJ\n0DziAq3HK44vcqB5SOTgsC568eo2fvxHxXA5DHVYIZAkguQr1k2u9m8v8IXOpbgl\nAbo+w3DOhDKd96sc/wJAXDNGflsaAEkXXvo60SzsY4njKCqElhm5xULV/ODEfvaz\nQ3zOLzUPmTe2aWKoI7d26UOofiui5g4W10FmfOUAPw==\n-----END RSA PRIVATE KEY-----', blank=True, max_length=2000),
        ),
    ]
