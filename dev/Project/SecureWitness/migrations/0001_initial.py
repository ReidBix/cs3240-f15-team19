# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('docfile', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=128)),
                ('url', models.URLField()),
                ('views', models.IntegerField(default=0)),
                ('category', models.ForeignKey(to='SecureWitness.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
