# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0047_auto_20151206_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(max_length=2000, default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCs6mjXSgKqaie/v8A+7JSmzJRX\nNQNEQRr9u/4vI7hwljHaT58AXHvrYxFgFVQf1GWmPK4lXqs7vTTOWDGZOx5T4hNn\nOy9BWoZ1ffekqP/v1RUG054onobma7c5HdIYqfKlKNpbGU8ObP2AerCQzFPb79Ol\njqbor0XKbL2VBKzKcQIDAQAB\n-----END PUBLIC KEY-----'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(blank=True, max_length=2000, default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQCs6mjXSgKqaie/v8A+7JSmzJRXNQNEQRr9u/4vI7hwljHaT58A\nXHvrYxFgFVQf1GWmPK4lXqs7vTTOWDGZOx5T4hNnOy9BWoZ1ffekqP/v1RUG054o\nnobma7c5HdIYqfKlKNpbGU8ObP2AerCQzFPb79Oljqbor0XKbL2VBKzKcQIDAQAB\nAoGBAKxA36wIGFu3YF2OIW8Nso/vIJ83OkfWK5M0oWRIS0Ys+QCnbJepifDVQcvb\ns2/54EEYFcs4YZAjTeV4ygABepUjAHxgXQbRquQkdOLUHRB1h+UrY7RflRzOiiQA\n0BqxFPDSzmqpT8/xCGgVREcNUdIOsasUcGTc/PsSpqAYaIm5AkEAuUsemnDE/OUn\nf98awVkv/m6bY3au8DuBY19D8Zhlc3wzAVnAytJRHvvKbL0y04OJPHHcEbmkRgcr\nhw+4S/P8wwJBAO7mImaQRAvv0NqKyjFu6Lv+CEwNWGaBzcb7LgbLCaOtd/tyVujx\nGa9gc3U94GqaktV/YJxmh4doO3jz/HStuLsCQDCP131ygK4nAKsqtcBmt4VfR6pR\nuJeNgOOiXBQ9dJlHu7Zm53hAlrIgG3VUQLXei2EkFiEvHjacOnQzUoHVeDECQBg3\nJZeF2g/nsCDm3pXiKx8bIdYrqCFD2QrpXQH9RK3doILRVTPpdHQNb8abjgrgPi/7\n6FwSHHzCOP0KpjVhgo8CQA2Fuka/gO4C19FINImoNxQEUobIi6XrQ3qTAzliJNux\n+GMa895GVEeEjInaj+Jx4ISrBOy1A/7sUURzUyZxdR8=\n-----END RSA PRIVATE KEY-----'),
        ),
    ]
