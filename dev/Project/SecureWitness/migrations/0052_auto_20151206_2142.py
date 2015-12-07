# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0051_auto_20151206_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='publickey',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDwCzgJp3J2AfB5Casf176ImU7P\n0OMZDY8sa29s5JDb25gRtSo61QZ0TzcGVs8+Htpfx8pnb7iyhiZKCx1KfbnBFTQq\nJYXKv7tFY2wR7usH6NKfusDlZLSl+67Ku8VOvVzvqancryMGHZAxtCtOg4CoR7ki\neHfwnazStkaHfRH/RwIDAQAB\n-----END PUBLIC KEY-----', max_length=2000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tempprivate',
            field=models.CharField(blank=True, default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXgIBAAKBgQDwCzgJp3J2AfB5Casf176ImU7P0OMZDY8sa29s5JDb25gRtSo6\n1QZ0TzcGVs8+Htpfx8pnb7iyhiZKCx1KfbnBFTQqJYXKv7tFY2wR7usH6NKfusDl\nZLSl+67Ku8VOvVzvqancryMGHZAxtCtOg4CoR7kieHfwnazStkaHfRH/RwIDAQAB\nAoGBAJa5hKtTMCT3HMbzkjcBYgslsH3/HMn7YJ40q5eFgYv7u+XKisS8RDw+DT/2\nvFS2TMp9ihMe7Kt0XpB5oB/JCBwEyGLQdSvVFpuC3ctceOgpDePsG8EOaIrBhh1F\n1P+Dgtw9nVI5gedNAYHf2OEQLwpe7GXWp3esMxhvGdy8uXIBAkEA8YEHJstA1f1N\n3VTKIFeOJiA7lpSdByTNa7XAKVyeBWvSGY0TyGXjmc73nXUkG+lQs4aozIU33kp8\nN8oZrOskRwJBAP5zwOdGjxmJApTurLdKC5sObk5wvmBtEdBS1IMHaq+HXDSSwrmW\nB+beaqKXk9zM25tyMTDKDZKoGjLy7WoWzQECQQC3pVJ24aDQGOsZH90EcxAZVfF6\nNFCkmgvLmE4kJdXUcYU3ANzGSxSkZYpOJkHrJ6TCn+fEfplZZHLJSdn0cGsJAkEA\ngD/Hkso1hiFQc9B4rUlc4CI95rtcuS1ANUgKZKBwXVhUWQs/qlq8UNj51kmf9UIr\nzgWYVYcBoFGqItPeZgJoAQJANrKdAeGzoX77dpBOGAewAmu7OBBAFt1rlCqw2IkB\nmc36SZ5XmmXbyKK2HGiHPeBaBqOFKQco7bhThXUVWhQlvg==\n-----END RSA PRIVATE KEY-----', max_length=2000),
        ),
    ]
