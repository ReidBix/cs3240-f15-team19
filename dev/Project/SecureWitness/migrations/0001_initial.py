# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=128)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('url', models.URLField()),
                ('views', models.IntegerField(default=0)),
                ('category', models.ForeignKey(to='SecureWitness.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('detailed_description', models.CharField(blank=True, max_length=500)),
                ('private', models.BooleanField()),
                ('timestamp', models.DateTimeField(blank=True)),
                ('aesKey', models.BinaryField(blank=True, default=None, max_length=2000, null=True)),
                ('folder', models.CharField(blank=True, max_length=2000)),
                ('group', models.ManyToManyField(blank=True, to='auth.Group')),
                ('sharedusers', models.ManyToManyField(related_name='shared', blank=True, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('file', models.FileField(blank=True, upload_to='files/%Y/%m/%d', null=True)),
                ('encrypted', models.BooleanField(default=False)),
                ('report', models.ForeignKey(default=None, blank=True, to='SecureWitness.Report', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('publickey', models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDKJ95B6vFQlbBTfnZN6d9RGfvh\n/GGg9QHlRd+BdHQ342mrdp5XurfxfxlvdDEmTUJK1ESckRmw7OzLcOEuc+Fix2Dj\ncCq62isJ322iAYMQ+a951d5Zz+LNd3eJWfdYyem0vDfFyTDMLQAUkBzrihZiFol8\nbRP7ZctHkRphqQUKIQIDAQAB\n-----END PUBLIC KEY-----', max_length=2000)),
                ('tempprivate', models.CharField(blank=True, default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQDKJ95B6vFQlbBTfnZN6d9RGfvh/GGg9QHlRd+BdHQ342mrdp5X\nurfxfxlvdDEmTUJK1ESckRmw7OzLcOEuc+Fix2DjcCq62isJ322iAYMQ+a951d5Z\nz+LNd3eJWfdYyem0vDfFyTDMLQAUkBzrihZiFol8bRP7ZctHkRphqQUKIQIDAQAB\nAoGBAJPatv9lU9wJr25R1ztDK5dItuZhThKIQDutcDxhrULXLIlA96zYnwKdYEAZ\nLn2CElNij1An/C9gCgz94WS1Uok69snJ+JNgZp1weLam8yz9PNta25Ja6Pew4X+3\n2wMJEI7kF4tltfK4tql6IvZjJhZPeZx+YFHiiAKazgARueFxAkEAzGvVCWj0dDHz\nOs8+QyPHxdvfaCUCXTwuQD3+ZK8BCkSk3iJdQVKn27C9x880zAEHZpn8T3gzkt7L\nE71k1bUQPQJBAP0ps6Qt7JGum07JPPSOMGcoX9jW18zp7xwAc7EXxNV0ENoia9R5\nYrXkFDSLAH4sSlzgQ2rsOjrQN344SU/0u7UCQQC82npMYTxGBMeS81ewK2QqdQEm\nc9qFTE3mZ9+YIN2zIMu3tMO2z6foHJaX++Po/KJbtbMVsBTlgRLYP8bicI55AkBu\ng4LRG98WpXNUzFJYq62DisN0hC0GXeSsg6H9X9PkHluw7a/GvAqUPnF3kmpvqeP4\ncUnc5ixxOi3PYsDWL461AkAnaZMfynX9z0EBJ+tKPhfv5AR7OT/tRCWDwxWTwna5\n4ZV3+6Iu0EUPSUWBFzWcBQbzNeXOXmSbmzLM1NWkXcJu\n-----END RSA PRIVATE KEY-----', max_length=2000)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
