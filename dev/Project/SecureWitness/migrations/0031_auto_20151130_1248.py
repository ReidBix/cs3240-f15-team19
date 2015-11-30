# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0030_auto_20151130_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(max_length=2000, default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC0AYFEKKWElJik6E0M6ch7we45\n/YUP9UpMzSeJtEZmLd2wQr9PujUS5OtpHiHZ0GkWKmjVtnvkOWPKbGANlABZtZ1Y\ntaD+joiMa++dwfJRIMlCvyH5DJvF26MN0aTqH6QN+UfshKYVu0kwppxwr6VghWU+\nlWiWlCCeryOoMld3lQIDAQAB\n-----END PUBLIC KEY-----'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(max_length=2000, default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQC0AYFEKKWElJik6E0M6ch7we45/YUP9UpMzSeJtEZmLd2wQr9P\nujUS5OtpHiHZ0GkWKmjVtnvkOWPKbGANlABZtZ1YtaD+joiMa++dwfJRIMlCvyH5\nDJvF26MN0aTqH6QN+UfshKYVu0kwppxwr6VghWU+lWiWlCCeryOoMld3lQIDAQAB\nAoGAKSk27+kDgD+icAMWq19CEtqTqPsJ1E5YwRsgcWKhvne6e7WnnYmM3VcvZYgY\nYYBAp2rnMgdaaSOeaAlEJZa0RWxMr5FmzJekn1t/cNSxGKxM8ozA6Enqwuwm+/7S\nCuTaVbXcBE6jGlH++S/my6QoNoz83Yd3Qac52IM00UPP3LkCQQC9jeRbCzn0KUZ+\nvG34IuQKQbUtjQAi4xB5whoqQU8crdbSEUsmipAObak97v7RLX5iEym+P0druo+J\n8GV6eR4LAkEA8xrD9RLqUFl7bV/NA6/4hs2LAurPzFJND3CLsUMeiEmjJWhFAgIW\nPmEYQSYOS5gxCgOhFUKkBBbv3bzwO45k3wJBAILA2O9wfAaPXkBYDGdo8fKdRrPo\nGlr2VEwY92GEcWTwCUoYgcVROXOqc170eDOkdRSD8Xx5O/P02cSl3eowl+cCQEAf\nASy1DoSe9YVFzYd5dK3prQ7Z7HFSC+1UnCPnNjhwY83MENeUwVU2uvUEGqUpwVWI\n24YGC8jgW+g6m4q55jUCQF8BuYKL/X5CNJwE0scySiXqAJ4ZQyq+urIpj/7ICW15\nkpYF7rBwMH1E1RxpECTs7czV5WbD5IzV9ya3QgAkyKo=\n-----END RSA PRIVATE KEY-----', blank=True),
        ),
    ]
