# -*- coding: utf-8 -*-

from django import forms
from django.forms import TextInput
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from django.db.models import Q
from django.db.models.query import QuerySet
from django.conf import settings
from django.core.exceptions import FieldError
from django.utils.text import smart_split
from Project.SecureWitness.simple_search import BaseSearchForm
from Project.SecureWitness.models import *
from Project.SecureWitness.forms import *
import functools


from Project.SecureWitness.models import Page, Category, Reporter, UserProfile, Folder

from Project.SecureWitness.models import *



DEFAULT_STOPWORDS = 'a,able,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,because,been,but,by,can,cannot,could,dear,did,do,does,either,else,ever,every,for,from,get,got,had,has,have,he,her,hers,him,his,how,however,i,if,in,into,is,it,its,just,least,let,like,likely,may,me,might,most,must,my,neither,no,nor,not,of,off,often,on,only,or,other,our,own,rather,said,say,says,she,should,since,so,some,than,that,the,their,them,then,there,these,they,this,tis,to,too,twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,will,with,would,yet,you,your'


if hasattr(settings, 'DATABASES'):
    DATABASE_ENGINE =  settings.DATABASES[list(settings.DATABASES.keys())[0]]['ENGINE'].split('.')[-1]
else:
    DATABASE_ENGINE =  settings.DATABASE_ENGINE



class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('title', 'description', 'detailed_description',
                      'private', 'group', 'sharedusers', 'folderOptions',)
        exclude = ('aesKey',)
    the_folders = (('hi', 'hi'), ('hey', 'hey'), ('test', 'test'))
    the_foldersObjects = (Folder.objects.all())
    the_folders = ( (x.title, x.title) for x in the_foldersObjects )
    print('hello there: ' + str(len(the_foldersObjects)))
     
    folderOptions = forms.ChoiceField(widget=forms.RadioSelect(), choices=the_folders, required=False)
    def updateFolders(self):
        the_foldersObjects = (Folder.objects.all())
        the_folders = ( (x.title, x.title) for x in the_foldersObjects )
        print('hello: ' + str(len(the_foldersObjects)))
           #folderOptions2 = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=the_folders, required=False)
           #self.folderOptions = folderOptions2
           #print(self.folderOptions.choices)
           #return self



class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ('file', 'encrypted' ,'report')

class folderForm(forms.ModelForm):
	title = forms.CharField(label='Title', max_length=50)
	choices2 = Report.objects.all()
	choices = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=choices2, required=False)
	class Meta:
        	model = Folder
        	fields = ('title',)


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

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture', 'publickey', 'tempprivate')



class SearchForm(BaseSearchForm):

    class Meta:
        base_qs = Report.objects
        search_fields = ('^title', 'description', '=id')

        # assumes a fulltext index has been defined on the fields
        # 'name,description,specifications,id'
        fulltext_indexes = (
            ('title', 2), # name matches are weighted higher
            ('title,description,id', 1),
        )

    """
    A custom addition - the absence of a prepare_category method means
    the query will search for an exact match on this field.
    """
    # category = forms.ModelChoiceField(
    #     queryset = .objects.all(),
    #     required = False
    # )

    """
    This field creates a custom query addition via the prepare_start_date
    method.
    """
    start_date = forms.DateField(
        required = False,
        input_formats = ('%Y-%m-%d', '%m-%d-%Y', '%Y',),
    )
    def prepare_start_date(self):
        if self.cleaned_data['start_date']:
            return Q(timestamp__gte=self.cleaned_data['start_date'])
        else:
            return ""


class UserListForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(),required=False)
