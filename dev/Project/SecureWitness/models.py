from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import RegexValidator
from Crypto.PublicKey import RSA
from Crypto import Random

class Reporter(models.Model):
     username = models.CharField(max_length=20)
     email = models.CharField(max_length=50)
     password = models.CharField(max_length=50)



class Report(models.Model):
    title = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=100, blank=False)
    detailed_description = models.CharField(max_length=500, blank=True)
    encrypted = models.BooleanField()
    private = models.BooleanField()
    #files = models.FileField(upload_to='documents/%Y/%m/%d')
    timestamp = models.DateTimeField(blank=True)
    user = models.ForeignKey(User, null=True)
    key = models.CharField(max_length=2000, blank=True)
    privatekey = models.CharField(max_length=2000, blank=True)

    def __str__(self):
        return self.title

class Folder(models.Model):
	title = models.CharField(max_length=50, blank=False)
	#files = models.MultipleChoiceField(widget=models.CheckboxSelectMultiple)
	def __str__(self):
		return self.title


class Upload(models.Model):
    name = models.CharField(max_length=50, blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, default="testfile")
    report = models.ForeignKey(Report)

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
    key3 = RSA.generate(1024)
    publickey = models.CharField(default=key3.publickey().exportKey('PEM'), max_length=2000)
    tempprivate = models.CharField(default=key3.exportKey('PEM'), max_length=2000, blank=True)
    #print(type(publickey))
    print(key3.exportKey('PEM'))
    print("uhhh squadron?") 
    def __unicode__(self):
        return self.user.username
