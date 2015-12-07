# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0005_auto_20151207_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='folder',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDWHgT/noUMRzQsDJEKR2vy6S7g\n9JzFTBEYcFtNfjm4vEzUUEF9uGeMevpukGe9tOX0bHYBQ6lw23sOTA9S7Iq/Noab\n7u2FMW6n4IKfWWIok8fKkj0BVFa5cJjp5Mnz1fASky9V9e+jDa5MX5Y7VLSto2wb\ntNif4waZPOpHQDa0cwIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(blank=True, max_length=2000, default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXgIBAAKBgQDWHgT/noUMRzQsDJEKR2vy6S7g9JzFTBEYcFtNfjm4vEzUUEF9\nuGeMevpukGe9tOX0bHYBQ6lw23sOTA9S7Iq/Noab7u2FMW6n4IKfWWIok8fKkj0B\nVFa5cJjp5Mnz1fASky9V9e+jDa5MX5Y7VLSto2wbtNif4waZPOpHQDa0cwIDAQAB\nAoGBAM2c6kPmH/HYdptOPgHW8CzGDARuIhW8pDYJv0O9UQS7njPMFff6m0Vl2xNN\njLG6A5EijndMWGxN9++UzqpdCCYxIjtjBjNEbb1oQEY3UZQApZxsvQHkVH3b0LrS\n6TivEkg5Fba4huim+YNgaX9j4eu/GkPViZA4OMLdX6IP1ehRAkEA5ZvsYXT6cUkH\nvYD7vq7LZ682fIMveO6/exbAz13FnVO3iPCBXydco8wxGx4TRJSHkcZ7SehuQu9H\npYnNgdc1pwJBAO66QtdC9+9FmUdO7sDuIzrx48dkMOP+5b20YNy3yRROY0aWNOE/\nhUCzW8QcpiyLs51NEV0gafsbbk0MgM6zfFUCQGNc46GVJuApc4ENtWPibsHS8ChX\n+Q5De3e/8/aJJQCdfvpy4fmUpiF4NvP+QuZVxIlQNIBaZoTu2bmIdfevc1cCQQDT\nuYZGfDKAl22V/L9rhMjiIl4uHQHvc8Y2NaAioS1JQSxzEgzcKQX5mBkvGWmX4F7w\nh8V6nqDgADgXRZuHt0/xAkEAo/6+sXkKpKIbEWLttYrK2AOsFQxMTs+ipyXJN1zs\nMqfYpsVLXnyEoDg2VLcwj1O8u8liCILuDC8WOhHhQL0E3g==\n-----END RSA PRIVATE KEY-----'),
        ),
    ]
