from django.db import models
from django.contrib.auth.models import User, Group
from datetime import datetime
from django.core.validators import RegexValidator
from Crypto.PublicKey import RSA
from Crypto import Random

random_generator = Random.new().read

class Reporter(models.Model):
     username = models.CharField(max_length=20)
     email = models.CharField(max_length=50)
     password = models.CharField(max_length=50)



class Report(models.Model):
    title = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=100, blank=False)
    detailed_description = models.CharField(max_length=500, blank=True)
    private = models.BooleanField()
    timestamp = models.DateTimeField(blank=True)
    user = models.ForeignKey(User, null=True)
    aesKey = models.CharField(max_length=2000, blank=True, default="")
    folder = models.CharField(max_length=2000, blank=True)
    group = models.ManyToManyField(Group, blank=True)
    sharedusers = models.ManyToManyField(User, blank=True, related_name="shared")


    def __str__(self):
        return self.title

class Upload(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, null=True)
    report = models.ForeignKey(Report, default=None, blank=True, null=True)
    encrypted = models.BooleanField(default=False, blank=True)


class Folder(models.Model):
	title = models.CharField(max_length=50, blank=False)
	#files = models.MultipleChoiceField(widget=models.CheckboxSelectMultiple)
	def __str__(self):
		return self.title


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
    picture = models.ImageField(upload_to='profile_images', blank=True)
    key3 = RSA.generate(1024, random_generator)
    publickey = models.CharField(default=key3.publickey().exportKey('PEM'), max_length=2000)
    tempprivate = models.CharField(default=key3.exportKey('PEM'), max_length=2000, blank=True)
    #print(key3.exportKey('PEM'))
    def __unicode__(self):
        return self.user.username
