# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SecureWitness', '0013_auto_20151207_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='sharedusers',
            field=models.ManyToManyField(blank=True, related_name='shared', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.RemoveField(
            model_name='report',
            name='group',
        ),
        migrations.AddField(
            model_name='report',
            name='group',
            field=models.ManyToManyField(blank=True, to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCl5TMHwHSjdTYcbTDfwCZtXQ44\nfkygdl2ZaRD5BAAzvUlbda8SF2jPVxty3SIx1B6YhyDCaT/xzsLAYfdy3DWLReb/\n7MFWALU1rbAETNGWK9ohRTwySl4eszjAWrHFMqqoO/3havCRy8jaJnHvcRPvrHmf\ncIz9KruAspNZPM22CwIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(blank=True, default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICWwIBAAKBgQCl5TMHwHSjdTYcbTDfwCZtXQ44fkygdl2ZaRD5BAAzvUlbda8S\nF2jPVxty3SIx1B6YhyDCaT/xzsLAYfdy3DWLReb/7MFWALU1rbAETNGWK9ohRTwy\nSl4eszjAWrHFMqqoO/3havCRy8jaJnHvcRPvrHmfcIz9KruAspNZPM22CwIDAQAB\nAoGADsM+r0npF0Ku9giheMfYo5LMWSqkFwNxgN1grUg13GTTylfGpI2AvjK6NpaH\nHHgL4Pbla2eCUTpdClGte4MtIHsBnDrJZdulRGjf0gPycmdp4PD1WlkvL5iqU47a\nhjw5CyVUp6wtmLru7DoAAdMXI/Dgrhi9kxHC5niWVOsq+sECQQDLXWDagkzZ87sG\nc6muKawh5FG3X14MBCUKDgFDiBZhwtTUzEf6eo4CaTVX7dzmWjN2hIS8CMuMHbEN\nNaaX0E1/AkEA0NUn1T9bzh/wugNWl2/Mz3qJMkh968KWo3bDmpVEd722rclvQ0fL\n7Y8Wi0HipbkTTJSUJW5BGZ0ZPNvgOvE1dQJASgxTMt0VDJtRszS0SQVFdwXCt2lT\nPj7YGcQls6g+thQSGPXVE6BCSyBx2vVyZLHdYT85cZomO3uoNy4c3dRsEwJAMHAQ\ngizk/WV5L5wQnKWI6uLwKaKY2nNS/21Pp25R6DgvxBWB4igoC9zxjLFmgavw5wVb\na2csYGWI8g3J78H89QJAHnm3hSGI0HeRhcU8FvbtNeGwC9WJkxzBo9cpQwCYR3nr\nEamv7vNRSStoPYE5bP7hw8J1RGs0MwNRRn98CrtD3g==\n-----END RSA PRIVATE KEY-----', max_length=2000),
        ),
    ]
