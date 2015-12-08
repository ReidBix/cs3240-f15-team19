# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=128)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('url', models.URLField()),
                ('views', models.IntegerField(default=0)),
                ('category', models.ForeignKey(to='SecureWitness.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('detailed_description', models.CharField(blank=True, max_length=500)),
                ('private', models.BooleanField()),
                ('timestamp', models.DateTimeField(blank=True)),
                ('key', models.CharField(blank=True, max_length=2000)),
                ('folder', models.CharField(blank=True, max_length=2000)),
                ('group', models.ManyToManyField(to='auth.Group', blank=True)),
                ('sharedusers', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='shared', blank=True)),
                ('user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(null=True, blank=True, max_length=50)),
                ('file', models.FileField(upload_to='files/%Y/%m/%d', null=True, blank=True)),
                ('encrypted', models.BooleanField(default=False)),
                ('report', models.ForeignKey(to='SecureWitness.Report')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='profile_images', blank=True)),
                ('publickey', models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDWY3kxrZDJkbPk+Ay5cpNnuroR\n+e4kZavFbyaX7+QSfMhPi0hY4jXB6VzOn2XYxyLgrTOAknKPvK+wbYKgC7X51iiF\nQeb6aoXqNVKH2Nowy1hWSOEEG1RXq/9vch7tFcr5SGfxZeFNBLFZGWRQHtwNAvA0\no6CeOo4H1xG2zs7s+QIDAQAB\n-----END PUBLIC KEY-----', max_length=2000)),
                ('tempprivate', models.CharField(default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQDWY3kxrZDJkbPk+Ay5cpNnuroR+e4kZavFbyaX7+QSfMhPi0hY\n4jXB6VzOn2XYxyLgrTOAknKPvK+wbYKgC7X51iiFQeb6aoXqNVKH2Nowy1hWSOEE\nG1RXq/9vch7tFcr5SGfxZeFNBLFZGWRQHtwNAvA0o6CeOo4H1xG2zs7s+QIDAQAB\nAoGADhbdeSFR+Z1EuFCA7ZMVEuUXo2TMfMHdxwzl+Wg/keN3eprJt2WuaL8AZWfe\nVp/HsAJR9yoosz+QQEUCJ6h9Xf4jM9hYVu0f/1DOTHQeaPUgsHtg7ZeyHxWOG+pH\nTobKrPyz+tVTshSRgUrxSh8a5K+fpPayNEKg4o3hlBHwRp0CQQDlHFNOtHbwgzpH\nIN8bNbL/tBinDAlJMB2itj5Ef/VvL9OqkDURBzMaMIzCLMsdUTNGq2uq8Q7xHr7f\nUhLxcnnXAkEA74zR+/uyDGlAUT2mdROi2lgBPS3IM7JMAXzvTDfpy74rTNSc7g1Q\nDGhRZWNSV17ChhnV99f68HJ73Fb48wkVrwJBAMS3uHP4kbNbCZvvBoGnbuUM7qnn\ntMVpkdiWoApS0BrCtvxZS6cuRltzWjiTG2c1xFAmeZDR3+F6Y6r+HpO/lgsCQCzo\nW10/3CsTeClCw3fjTH5eTS0o7gUzAaitwTaqrLuzVO68VQcTm9QXolq9eexDKXh2\nU3R5GuQEsk+mRllZdKUCQQDAkI77Of2VIg7ZSsAWM/Wc4e4LFjmHMx2rtkv+HDfw\nDsnUKn/R+Srj/trIQWrREO6t2FSP1s8gi3YkhG31vUVN\n-----END RSA PRIVATE KEY-----', blank=True, max_length=2000)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
