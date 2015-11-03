# -*- coding: utf-8 -*-

from django import forms
from django.forms import TextInput
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from Project.SecureWitness.models import Page, Category, Reporter, UserProfile

class DocumentForm(forms.Form):
     title = forms.CharField(label='Title', help_text='Title', max_length=50)
     description = forms.CharField(label='Short Description (one sentence)', help_text='Short Description (one sentence)', max_length=100)
     detailed_description = forms.CharField(widget=forms.TextInput, label='Long Description (paragraph)', help_text='Long Description (paragraph)', max_length=500)
     encrypted = forms.BooleanField(label='Encrypted', help_text='Encrypted', initial=False, required=False)
     private = forms.BooleanField(label='Private', help_text='Private', initial=False, required=False)
     docfile = forms.FileField(
        label='Select a file'
    )
#     created = forms.DateTimeField(label='Timestamp')


class CategoryForm(ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Category
        fields = ('name','views','likes')

class PageForm(ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    class Meta:
        model = Page
        fields = ('title', 'url', 'views')

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data

#username, email, password
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','email','password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

class ReporterForm(ModelForm):
    class Meta:
        model = Reporter
        fields = ['username','email','password']
