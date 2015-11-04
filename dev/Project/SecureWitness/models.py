# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Document(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    detailed_description = models.CharField(max_length=500)
    encrypted = models.BooleanField()
    private = models.BooleanField()
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    timestamp = models.DateTimeField()
    user = models.CharField(max_length=25)
	

"""
#Creates user named Reid with email and password
userReid = User.objects.create_user('Reid','rmb3yz@virginia.edu','password')

user = authenticate(username='Reid',password='secret')
if user is not None:
    # the password verified for the user
    if user.is_active:
        print("User is valid, active and authenticated")
    else:
        print("The password is valid, but the account has been disabled!")
else:
    # the authentication system was unable to verify the username and password
    print("The username and password were incorrect")
"""

class Reporter(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username
