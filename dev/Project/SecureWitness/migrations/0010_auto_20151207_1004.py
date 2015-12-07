# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0009_auto_20151207_1003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='folder',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCpk8JNR3zxKksGD8xprcYhClY5\nKI5/gFsFQohP8o6mLLXe0EjZIm/av+omaF2e0thOnoiX3peeOkCtA8Mna/d5oNig\naloyX9UC69o5vJaF0NpG40g2Ilo63dW/nEE1hjsckz5J/uWUHwbYKX0HMlz3yexG\neyK0oL4GwOxFPqs0bQIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICWwIBAAKBgQCpk8JNR3zxKksGD8xprcYhClY5KI5/gFsFQohP8o6mLLXe0EjZ\nIm/av+omaF2e0thOnoiX3peeOkCtA8Mna/d5oNigaloyX9UC69o5vJaF0NpG40g2\nIlo63dW/nEE1hjsckz5J/uWUHwbYKX0HMlz3yexGeyK0oL4GwOxFPqs0bQIDAQAB\nAoGAbFK+466u2T8y/YRKB5fB4IlB2vFVVY0gl5OQj8FZ7jzRUKusXUfqO8osQKya\nYUI+ero6dwjxwVlkxyCIIT6Ork7/GF3JH3WnhZF1nL0I6J67WdtskWtzISkjDdVf\nYY2fWLQ+EezH2PEyyueQ83oh5baWONVyt4ryeQUYdPsse+ECQQC3czUhCZVFX7pn\nPDXfxmRY2u6JBFK4fZEsm6sU+jFHNjmuhzHIQsbFvkoQfTVBwJ9Njvchks9k7W+D\nfaw4EYZXAkEA7KQKff4zJkEQyrNa+TOAknBleIHwR4p/WaI84pRqQ2qaE/rPvriu\n9n2PQd+DmX/shAVa0tzdkUQqTAzXnx/42wJAS+wXOeQQbhSvPZhyp3khAJEjFXu/\njHETSwXl6RmemV08xBlZpgrU3vPhDS/0gZDpnRyk9LUgtiF5/E5fnxjJowJAWWoG\nWOMC+rJdIOoyNrUiILL9dFJMswt+4SRvMwH3QO/3thLwClWILrT0u2Q0OnzepmfL\nkJ9JzQjfnoq/sm2HPwJAaWDM7XeGZ9honLfXnY8mIQJckbfFr/e3azoFdWxoT323\nsADo5G49yYb4XdcCwBeYsNjDfig5sXZaP6C5uOrPLQ==\n-----END RSA PRIVATE KEY-----', max_length=2000, blank=True),
        ),
    ]
