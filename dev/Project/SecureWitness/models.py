# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import RegexValidator

class Document(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    detailed_description = models.CharField(max_length=500)
    encrypted = models.BooleanField()
    private = models.BooleanField()
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    timestamp = models.DateTimeField()
    user = models.CharField(max_length=25)
    key = models.CharField(max_length=2000,blank=True)

    def __str__(self):
        return self.title

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
    uKey = models.CharField(validators=[RegexValidator(regex='^.{266}$', message='Length has to be 266', code='nomatch')], max_length=266,blank=True)
    rKey = models.CharField(validators=[RegexValidator(regex='^.{872}$', message='Length has to be 872', code='nomatch')], max_length=872,blank=True)

    def __unicode__(self):
        return self.user.username
