# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0011_document_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='key',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='rKey',
            field=models.CharField(validators=[django.core.validators.RegexValidator(regex='^.{872}$', message='Length has to be 872', code='nomatch')], blank=True, max_length=872),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='uKey',
            field=models.CharField(validators=[django.core.validators.RegexValidator(regex='^.{266}$', message='Length has to be 266', code='nomatch')], blank=True, max_length=266),
        ),
    ]
