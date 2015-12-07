# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0055_auto_20151206_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC+QqPnJ7oU0mvoB93UXQtig3aH\nr+iaCy0OhvKXcFtuv06OCviVR9qWFKIEXqfjOILgp7xDyxB8Q1qT5OLrDY4XMDR4\n2o4ZHdsm8/DUGOetgVvY56GzpZFG/rFWH7QGnlVdSV/19mCUuu2/F9MoX5NeNz5m\n574YUBZWg4pDFlZ0gQIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXgIBAAKBgQC+QqPnJ7oU0mvoB93UXQtig3aHr+iaCy0OhvKXcFtuv06OCviV\nR9qWFKIEXqfjOILgp7xDyxB8Q1qT5OLrDY4XMDR42o4ZHdsm8/DUGOetgVvY56Gz\npZFG/rFWH7QGnlVdSV/19mCUuu2/F9MoX5NeNz5m574YUBZWg4pDFlZ0gQIDAQAB\nAoGAQvLGI+/JvcvxZntmJnT7LZYe3k4a5iGqoCMCOCG0OrsclETuBfF7zDXEcQ8x\nunXHL/A2AhDxYxh8RfBTnOxvI8NF3U4DKbXjkaylnQzgq2d2tYuqVMiMXhjZDBJl\nF91BhhkUTJba+JH0mL5DAgyhO52TWolKuoSTP+23GtSRJXECQQDDwIuIAE2tfi8K\n26oUVVhPLFCJ0n5V6+DGsE54cKJawR53pFRfW1TifidrVIr+JQjrylM1b5QQsZK3\nXphRkH8dAkEA+NFkF+bzKF6/2Rrq9XGugIYtAyBzkRtidADXke+4eOSReHcnIhZo\nJJNlgo7L64NbEcMMVFKgRjZS48VasJHZtQJBAIuRkiqyxK+Jg3MDcb2zqBYzK21I\n5ojOeGJRvHFFJYz9moKFaR7gGKKwfdyZ18wijbzIchFsb66DXW9eg83L78UCQQCM\nDI/iREQpPOuPL++AJ3SpMtyzHdjunBNWaALuSZfzs/ONcsO8FBCaRbylN+rfrRfd\nb4PJEpjT7E/LlJHvQKjhAkEAr3/ujgvq7+5FnfOHghvO0PQKwT4np4b3bunZBpx9\nJn4AtHb3x9owpwYOgOicEDX8b1F+5tTdd5CVqyQw08LKZw==\n-----END RSA PRIVATE KEY-----', max_length=2000, blank=True),
        ),
    ]
