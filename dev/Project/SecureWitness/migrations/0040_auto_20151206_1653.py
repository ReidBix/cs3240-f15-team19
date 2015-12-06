# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0039_auto_20151206_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reporter',
            name='email',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDelL30ylpcTjSop+RMMSiIzg6R\nrg7QfxSZ05GeHQNXArgZijFkiRwONJoDAMkS0QxjPnj3U5lLMyMdOplquovO0H4p\nTg3WvLNn2MbApmvfcg4aA0kyVhCxQvJuueemqArR+5BMbZavzYcDQ3MuR3IzZk/D\nIR8Z+b4JyJUgBEoJjwIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQDelL30ylpcTjSop+RMMSiIzg6Rrg7QfxSZ05GeHQNXArgZijFk\niRwONJoDAMkS0QxjPnj3U5lLMyMdOplquovO0H4pTg3WvLNn2MbApmvfcg4aA0ky\nVhCxQvJuueemqArR+5BMbZavzYcDQ3MuR3IzZk/DIR8Z+b4JyJUgBEoJjwIDAQAB\nAoGAX67XffzjHV0tO/d4p9xWDYFvN+b4TV7j70DJD4xvXB86HxiOJSbf3ad1MadL\nyP/+8Ebx33ibpH0mMjF3tC7fXEoVuP7hY7olYXZRlNDXbBPFPPdOyVVDNjAnxTQz\nyU2SwVbP7ETdwx15lBWUAAzSoVPHP57wY7WpAWtzbYnp1vECQQDgE0rgf8Bs/FJE\ntnkdGjPkH9UmpVjUYsIOGQSh6MnCJKliOhUedyhcm/B01gtclqXzvgsoXsHBex6M\nnT0+6orXAkEA/kryTeAP3TG/2ROokdAczOYX5VaY/+E+M/ferTC+jeJ2CjWmBgUv\n1XvULhZPpNH0oe7alM51n7mud51o1VEYCQJAJ3L+EbwsEoPxr+s4M2lzjUwVaLJf\nizS/2V+KMz8aljWCJKr5IN31myhREyDD608SdHEW4cqc7gVRAYyFRdhhDQJBAJ42\ndREcseIWXN2rjHrEN9cH5aArw9+X/YKJ2oJ4zGYsmvJ5NIWUXpF9jKLsALt0YbcK\ni/Z/idFJzpHfXuUxojkCQCUlfYCVltzNIZ9t6fsdPUS/N/V6ijw1MpFleFp5EAwl\nYXgFsmkeJMuOR9x+GveVWQv5r3n91o29qEly7ybuySU=\n-----END RSA PRIVATE KEY-----', blank=True, max_length=2000),
        ),
    ]
