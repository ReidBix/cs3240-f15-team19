# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0058_auto_20151206_2356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDscoMSfNnS7nhVFdX151Z7o7Uk\nuFQ5+tFCL6ZF6dbbxxiaOGHljvZSe7clIPsFJbbyyIVr71Hp2qLqpU2Gg0sYmyHI\nTVmI/RL3sL6qfm0F+eJ4XnYeTVhsinSkCJ27ioEyM8HOqGSnfxtUPQOAhf7kcrdt\nynZJXVuLajQMePxq0wIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(blank=True, default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQDscoMSfNnS7nhVFdX151Z7o7UkuFQ5+tFCL6ZF6dbbxxiaOGHl\njvZSe7clIPsFJbbyyIVr71Hp2qLqpU2Gg0sYmyHITVmI/RL3sL6qfm0F+eJ4XnYe\nTVhsinSkCJ27ioEyM8HOqGSnfxtUPQOAhf7kcrdtynZJXVuLajQMePxq0wIDAQAB\nAoGBAKKpzN5FIh1ojUQLt5xqQCbi4tWWMeuJT7i2yy7BxlyARb6jF0Yz6eWo0sAq\nRkauQYQYyyEMDVBSZ04B1qm5XUkHvAv6XXqQr1KrhoZ8jOibHSg+l1IoNBd6wkkH\n8OdAKIc80jtzm55SpQNLy2ZnQGLFBwXg1yrs2wctATutUjFxAkEA9WbW/BZGTcWC\nBDlHjOR/8eiL+2dvnt96gPo/RpKHZQTo39trkJQs1rH+BLwaBXem3Bve+xWNTAZf\n3FFQBFC//QJBAPaorB9eApcUqQVxlNjqsLUIZ/FFnmk12B4dCVcdhpATKquGxHMW\noynaDrqQLiwXZPxhyMuCyA9BOotIZzmqRw8CQEkCga+aSOxWeKodCIaIbPBhyVPQ\noEraHi5FRZIPgiyx2z7Onx/ylayCZBqwg+VghcoymJKHBPS7aMW5g17lT1kCQQDS\nzHo1YHmkNpLwxQ4piAE25hU2/IGSduLZcYVO/zvGG6tG5ik0Fm+hT+twg9IB+ohi\nrQsW6hEiAGQRLvKRNLX/AkBteXt6bt1QoujYASNfuXmOr1Br6t4v1bPKw1TDsrwa\nIYPpxLMEp4mxQLZjbd/3RV6sLxXxtkQMzXoWKeUmrJsq\n-----END RSA PRIVATE KEY-----', max_length=2000),
        ),
    ]
