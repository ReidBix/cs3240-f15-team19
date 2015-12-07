# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0003_auto_20151207_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCsJ5s403uWpHeEcJeLoGdYc/md\nbAzkE+YhufUcse30c3K7Jigab3e9yfPlMWRVhOWQrWxnEmkV4u+cNNXXfXtOjAnv\nzwdxpqN2piJhXU9/HkB5YprF35F29ABsE39qUhJE55VbTgxmNL/sK2R1n2SW+bvO\nswmLv4iiDeHX47iblwIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(blank=True, default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICWwIBAAKBgQCsJ5s403uWpHeEcJeLoGdYc/mdbAzkE+YhufUcse30c3K7Jiga\nb3e9yfPlMWRVhOWQrWxnEmkV4u+cNNXXfXtOjAnvzwdxpqN2piJhXU9/HkB5YprF\n35F29ABsE39qUhJE55VbTgxmNL/sK2R1n2SW+bvOswmLv4iiDeHX47iblwIDAQAB\nAoGAXriQDE04M+OcKw+0IkwIcL+m+PnJgfh859OkTLyNm7Glz9knuZvZO2CRxGpP\ntUog8WCqQ2/6x+MMSVs8yYsuO1roh3MlBsfeqGtnsijNMkyhCFSJINqc1ar4416P\nJ52+YoKj+ED4gn2mHfVp2mSha/fSupLxokXPVN1amOei2EkCQQDDFoUccSsHJVb6\n404G92hWxBaMsnY+uMR4p5dECY6Q3ekxkVMzyp9YwgRDhW3QCCTdNKubLXWvfJip\n99LuP1ONAkEA4egFA533EvoLAk5y8UCL4RWQjVrLX78aAfwPXRr735q+vczrTrlH\nbDEquOUzihJQ3OPspk8o+PgstmDc3dHwswJAVwH7OhUq+JPpuBmamjbLvS7VU8jg\nPdcQITO1ni2Y/PlL4MSM1COBcAeP+UFQGaEYN+QeySW8QBkUyXFzDLkHnQJAZrJU\nfTV1mcHj+VNye2wtatCj2y7YX5l/mEFfNqNKt3cgmSYsHqip6GxdkJpZmL4E1rYi\n4eQAq1Ye9XYJUinbcwJAJNZPxcNHLBDPxGlfCoZBpHraryR9cZepjRqAaqRYDMoJ\nqMHWp2r1YRmjM9qwAjpPvo7pUnFoq+DtsOUXZr9bwg==\n-----END RSA PRIVATE KEY-----', max_length=2000),
        ),
    ]
