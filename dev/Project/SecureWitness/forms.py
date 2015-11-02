# -*- coding: utf-8 -*-

from django import forms

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from Project.SecureWitness.models import Reporter

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )

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