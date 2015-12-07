# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SecureWitness', '0056_auto_20151206_2328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('detailed_description', models.CharField(blank=True, max_length=500)),
                ('encrypted', models.BooleanField()),
                ('private', models.BooleanField()),
                ('timestamp', models.DateTimeField(blank=True)),
                ('key', models.CharField(blank=True, max_length=2000)),
                ('privatekey', models.CharField(blank=True, max_length=2000)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('file', models.FileField(blank=True, upload_to='files/%Y/%m/%d', default='testfile')),
                ('report', models.ForeignKey(to='SecureWitness.Report')),
            ],
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.DeleteModel(
            name='Reporter',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCzaXPlpYvwoMZVdfGD0l1mjhmr\nQjbZ2FYgBPLafBbTtMayQ0qKw12QHKTh1y2OpLvvfGTG+pmZ/SyvS9t2kPv4qdYP\nM2b+5kL2aTnkKIOPUb9BF67MiTt5OXicFjx3nDWD9VoqR2MkmEUWpbpHa8QsDNWz\nThQuicEZmfA7JORHZQIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(blank=True, default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQCzaXPlpYvwoMZVdfGD0l1mjhmrQjbZ2FYgBPLafBbTtMayQ0qK\nw12QHKTh1y2OpLvvfGTG+pmZ/SyvS9t2kPv4qdYPM2b+5kL2aTnkKIOPUb9BF67M\niTt5OXicFjx3nDWD9VoqR2MkmEUWpbpHa8QsDNWzThQuicEZmfA7JORHZQIDAQAB\nAoGAddl6GMpSjwB851wvBgEj+x6ye81lzFkP0b6Oa7gBIpVnw2bySw4joms+X18B\n/OX20UwrwoyQYxdrx8YTZeG8sLOOunhpaGyUn2USAvCgL/gummIIQp1nGc8O5lC6\n0IjzmoWhQ9eaS8TqRM0qHBklRl6js08FFZIIxmGrJWucTuECQQDKJ/BfWpXiClF8\nS6XxZcDbAyP1+o6BpwhMT6XMChnwNd2Vt/c9BxZhl5VsL/xXLxRKBU4Usfo8OnrA\nzQ3ZynV9AkEA4zKzw0wcxI+6YItQP3V7NSgyp6x42DdKYoOfmEzSPZ7yldJAf6hc\njGGsi0Ks643GedRizjWqdpqLoz7DYL+eCQJBAJ64vQIhHY1cjJ4Kxz/BpKpQzOtU\nzo79loZUAtkxFSyFHnVu+6/u4KO/YJKRGo9ZZ5S2lZeqJc8kGz1Fwpo9XAECQQDb\ndryiqEEZtmSooaoQwqETRhM4WKga473cz5w4d+yWTZWzF3fqWG2dxTPxCaUTnM3e\nHUScQMa67qp4NEZyjGZRAkAb5bkRNeqpc6TdyLF9SVzsyTqZ8UQovoCzTqk2ZbF8\npmYCaWtBSNqmtY3//+7qB8TC8kFy38ExJ3PdrtKSEJ5N\n-----END RSA PRIVATE KEY-----', max_length=2000),
        ),
    ]
