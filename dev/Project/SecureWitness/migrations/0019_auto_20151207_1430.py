# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0018_auto_20151207_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCZfjDo6SC4XS6o4+hrvweCdIDR\nRC6WRM5cZBtjy9KtIHkodhlUP0TtYfG/c0ax7n8GQmWaKHvlufMgYST7IbSDcMgK\n54SMHmSAN+E1+iRKeTVLQ/NjZjwGbvBzdOYL+9cz9UgSMylKJXeiR5Chl35fIrt6\nzD824+AjNxoFwprZYQIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICWwIBAAKBgQCZfjDo6SC4XS6o4+hrvweCdIDRRC6WRM5cZBtjy9KtIHkodhlU\nP0TtYfG/c0ax7n8GQmWaKHvlufMgYST7IbSDcMgK54SMHmSAN+E1+iRKeTVLQ/Nj\nZjwGbvBzdOYL+9cz9UgSMylKJXeiR5Chl35fIrt6zD824+AjNxoFwprZYQIDAQAB\nAoGAZB3uUw00vWxyMdEuWZEpmcrZ9yVs6bEJlTPqtaZNzYT/4gdeMBhwohGfuIu9\nUfPJQNDwKqQ7ZDVswvL6Rx/N+GdAnxA+KeSliS8NpT6I0Pbxp8Np62DMMcRJmv0M\nkqeLUoc4iAOB2P5RvOG443Vaj05THSyfIah/2QcBN4fatZECQQC+0oihJuYjCyTs\naxc6Jbz3XwbsqAeUTmEEczbHzjpML40BBMorSJzibYUkzutZEr4R0R0WDKDlnMXY\nBFW3BJMNAkEAzeuT43XujGAbX6Nw5W98Mfk/tI8FQTUVD5WJoJjiRKqdu/fsgT73\nXYd8jq5NJXD8MPJYlkIF7kCTqoRo9WvapQJAAoZAfnlIRCBqnaIRDZjgNhmQuuLC\nLukWiXuItv34cXeTkvbgQdBVGv297C28mVIRJ6UvkFIccs0vJNtx0tkBpQJAQ4j9\nyd4FzLhAgg9imX0E6Ibso9U8TfSQ4bmTl75Mh2TFsr5PLNxv2Jb0/P6hgqQZshvp\nfe5Nb6RySbx/h+5FmQJAD0FHU3jX3/PQ4QiELU+jqdIABxjyclJsvG634LMKoQuD\n/rYkz+isfQTwynDmIvoCasqwuzlkUUOhip+L80uK0A==\n-----END RSA PRIVATE KEY-----', max_length=2000, blank=True),
        ),
    ]
