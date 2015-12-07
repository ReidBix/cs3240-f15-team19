# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('url', models.URLField()),
                ('views', models.IntegerField(default=0)),
                ('category', models.ForeignKey(to='SecureWitness.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('detailed_description', models.CharField(max_length=500, blank=True)),
                ('private', models.BooleanField()),
                ('timestamp', models.DateTimeField(blank=True)),
                ('key', models.CharField(max_length=2000, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('file', models.FileField(upload_to='files/%Y/%m/%d', blank=True, default='testfile')),
                ('encrypted', models.BooleanField(default=False)),
                ('report', models.ForeignKey(to='SecureWitness.Report')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('uKey', models.CharField(max_length=266, blank=True, validators=[django.core.validators.RegexValidator(code='nomatch', regex='^.{266}$', message='Length has to be 266')])),
                ('rKey', models.CharField(max_length=872, blank=True, validators=[django.core.validators.RegexValidator(code='nomatch', regex='^.{872}$', message='Length has to be 872')])),
                ('publickey', models.CharField(max_length=2000, default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDcmfv02Fg8VXPJXKPsQVAEa1Wu\nm30rQzBfyNNWMTnsbhZSiUyotwIV29n/FRx8w1Pz2r2ZLeKnKAY45knj9ZlMUYJc\ned2zw4heK7i8xQIE4uYV0Az8W6JtnfwKYtOuBS5faz0gIo9XLJnnFKXMuS5cJf5x\ngbofCgdI//mFu1Pi/wIDAQAB\n-----END PUBLIC KEY-----')),
                ('tempprivate', models.CharField(max_length=2000, blank=True, default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQDcmfv02Fg8VXPJXKPsQVAEa1Wum30rQzBfyNNWMTnsbhZSiUyo\ntwIV29n/FRx8w1Pz2r2ZLeKnKAY45knj9ZlMUYJced2zw4heK7i8xQIE4uYV0Az8\nW6JtnfwKYtOuBS5faz0gIo9XLJnnFKXMuS5cJf5xgbofCgdI//mFu1Pi/wIDAQAB\nAoGAbZa9eQPkyYw16glwkZRcmOVtekFaLBzDskHE4yOvP8nsovH8ODA6A/vkzviA\n32X1lcXLvIXz+9BBTxDwEiPXFAuPcxMP6YAbkUclKnvc/Uowa6JxOmy1cNjtK5eY\nBEiO9nXIKl5+4lZ5ueD6ougbjR87YbfmWR+40zaKXVed0gkCQQDmzni1lt32sPkK\nrXz8RFkfeEbdFde7tKD69vk3K+u+uEBimHs5soUdEnu206ieA5xmBHZvZdxEfND0\nbPtr72YVAkEA9K5ZXRrKEXZgbd8BmCqnG2Vlb05itGPMCUugck8COLj7NhpUmyo8\nAXQWyv8Uac94038msazMrLmp+R8B/LXdwwJASkcaO75Qsopjq1cHyRup3uHTVGUq\nJ2NLB1kh/OpqlNcxCUnvJjNYeXGwVLcrJacd1wsKnnEWgQf2KyNDionhvQJBAL2d\nr5s7e4T0293JiI7H3yCX/3e2oz9wZ1p8xSZQnEQg9m0DErX8kOv/bvp5mvQ02Enu\nq6ndY/AnIdXxdbTFq8kCQF+u4BhkQi7mqIhUwq5xw23R3xEWVHC1hHJmVsns8aEy\nj4P69AxH/3sXOLu2KAtPxZW3pzkCM0kDOz3kP1fHJBA=\n-----END RSA PRIVATE KEY-----')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
