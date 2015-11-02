# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from Project.SecureWitness.models import Document
from Project.SecureWitness.forms import DocumentForm

from Project.SecureWitness.forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import login

from django.http import HttpResponse

def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('SecureWitness/index.html', context_dict, context)

def about(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('SecureWitness/about.html', context_dict, context)

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
