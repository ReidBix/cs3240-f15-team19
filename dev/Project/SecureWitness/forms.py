# -*- coding: utf-8 -*-

from django import forms

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from Project.SecureWitness.models import Page, Category, Reporter

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )

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
class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','email','password')

class AltUserForm(ModelForm):
    class Meta:
        model = User
        exclude = ['email']

class AltUserForm2(ModelForm):
    class Meta:
        model = User
        fields = ('username','email','password')
        labels = {
            'username': _('USER')
        }
        help_texts = {
            'username': _('Any user name works!')
        }
        error_messages = {
            'username': {
                'max_length': _("This user's name is too long."),
            }
        }

class ReporterForm(ModelForm):
    class Meta:
        model = Reporter
        fields = ['username','email','password']