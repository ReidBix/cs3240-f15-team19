# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from Project.SecureWitness.models import Document, Category, Page
from Project.SecureWitness.forms import DocumentForm, CategoryForm, PageForm

from Project.SecureWitness.forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import login


def index(request):
    context = RequestContext(request)
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    for category in category_list:
        category.url = category.name.replace(' ', '_')
    return render_to_response('SecureWitness/index.html', context_dict, context)

def about(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('SecureWitness/about.html', context_dict, context)

def category(request, category_name_url):
    context = RequestContext(request)
    category_name = category_name_url.replace('_', ' ')
    context_dict = {'category_name': category_name}

    try:
        category = Category.objects.get(name=category_name)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
        context_dict['category_name_url'] = category_name_url
    except Category.DoesNotExist:
        pass
    return render_to_response('SecureWitness/category.html', context_dict, context)

def add_category(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    else:
        form = CategoryForm()

    return render_to_response('SecureWitness/add_category.html', {'form': form}, context)

def add_page(request, category_name_url):
    context = RequestContext(request)
    category_name = decode_url(category_name_url)
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            try:
                cat = Category.objects.get(name=category_name)
                page.category = cat
            except Category.DoesNotExist:
                return render_to_response('SecureWitness/add_category.html', {}, context)
            page.views = 0
            page.save()
            return category(request,category_name_url)
        else:
            print(form.errors)
    else:
        form = PageForm()
    return render_to_response('SecureWitness/add_page.html',
                              {'category_name_rul': category_name_url,
                               'category_name': category_name, 'form': form},
                              context)
def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('Project.SecureWitness.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'SecureWitness/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )



"""
def addUser(request):
    context = RequestContext(request)
    isRegistered = False

    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            newUser = form.save()
            newUser.set_password(newUser.password)
            newUser.save()

            login(newUser)
            isRegistered = True
        else:
            print(form.errors)
    else:
        form = UserForm()
    return render_to_response('adduser.html', {'form': form, 'isRegistered' : isRegistered},
                                  context_instance=RequestContext(request))
"""