# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0048_auto_20151206_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDMlea1F8KQ7IAgOyupUKx5ntMZ\nqH2B0JWFi6zvtX7ml+8XhgFBaqcsGdjHGYJb4jlR+i6gbUJMwR5/kjipoh0K2VCe\nVJJA43n9ApYyjoLrf/y4ENpcQluTkQBARW+Rw/ptQ/MHJ/u5M/l7XvmI1mT1Ex1O\n0Ow6bmIsxHfG7eERBwIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQDMlea1F8KQ7IAgOyupUKx5ntMZqH2B0JWFi6zvtX7ml+8XhgFB\naqcsGdjHGYJb4jlR+i6gbUJMwR5/kjipoh0K2VCeVJJA43n9ApYyjoLrf/y4ENpc\nQluTkQBARW+Rw/ptQ/MHJ/u5M/l7XvmI1mT1Ex1O0Ow6bmIsxHfG7eERBwIDAQAB\nAoGAGwCmBLzwF0S/3IEy0BQvz5Wg80AD4MBxG8FFwBXKfBENo6MyQzoaen2m2RCK\n3inLuwA0a0RAffT3W4snI2ycPHexCrLJhKE+ZGaxRpCf/Dr5NlOPujk02wiH+SDY\nDOEg97Xl8n7doXarwTUQP5RtufRK0cHoQJEvW41ooqlXHHECQQDRlS5ReqKeTaF1\nty9kCeiypBgXDg8imt/zSi8f0YhhUYnAAd/1I+olXf9cbPCRewjlCvSR7PDoH3CC\nFoam62htAkEA+eVkam7Szx3dzAmIho6mQjSKDWN7Fm2IEd9zjpY7TreLDwzm5LUd\nAJovkgsvTdAapOdg6cMipx0gn8b/dsrewwJALrfzgEQ3FdS2RjhUfxdaYOAFYrZG\nl28wttn1kUEzBoaXj06brtiXrEa80syR/8wOWohLpm/L7+J6QPVmhLT7LQJAHzLK\nZJdNblo2NKEEEHiCvUU97wn6dgRatpCFJsoOwXccv1ZHBUqvQkH9qmgHEdnnWash\naE3aZ661Qf1gK36MbQJBAIbXGfMHdebCPcrUo0LZbCWpKUHCA2QwGwZoFM5GdOB+\nv+wy8D8NNuR79lgSvsp7nLO4O1Vr4MVRKKaDmd046PA=\n-----END RSA PRIVATE KEY-----', blank=True, max_length=2000),
        ),
    ]
