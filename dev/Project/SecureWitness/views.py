# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from Project.SecureWitness.models import Document, Category, Page, Group
from Project.SecureWitness.forms import DocumentForm, CategoryForm, PageForm, UserForm, UserProfileForm, DocumentSearchForm, GroupForm

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import pdb;
from datetime import datetime

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


def list(request):
   # pdb.set_trace()
    # Handle file upload
    if request.method == 'POST':
        encrypted2 = False
        private2 = False
        timestamp2 = datetime.now()
        if 'encrypted' in request.POST:
                encrypted2 = True
        if 'private' in request.POST:
                private2 = True
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(user = request.user, docfile = request.FILES['docfile'],
                              title = request.POST['title'], description = request.POST['description'],
                              detailed_description = request.POST['detailed_description'],
                              encrypted = encrypted2, private = private2, timestamp = timestamp2)

            newdoc.save()
		#used to be newdoc.save()
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('Project.SecureWitness.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form
    
    squad = Document.objects.filter(encrypted=True)
    # Load documents for the list page
    squad_again = ""
    user2 = request.user
    if str(user2) != 'admin':
    	squad_again = Document.objects.filter(user=user2)
    else:
    	squad_again = Document.objects.all()
# Render list page with the documents and the form
    return render_to_response(
        'SecureWitness/list.html',
        {'documents': squad_again, 'form': form},
        context_instance=RequestContext(request)
    )

def register(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response(
        'SecureWitness/register.html',
        {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
        context)

def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/SecureWitness/')
            else:
                return HttpResponse("Your SecureWitness account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response('SecureWitness/user_login.html', {}, context)

def search(request):

    if request.GET:
        form = DocumentSearchForm(request.GET)
        if form.is_valid():
            results = form.get_result_queryset()
        else:
            results = []
    else:
        form = DocumentSearchForm()
        results = []

    return render_to_response(
        'SecureWitness/search.html',
        RequestContext(request, {
            'form': form,
            'results': results,
        })
    )

@login_required
def auth(request):
    context = RequestContext(request)
    usrs = User.objects.all()
    usrs = usrs.values_list('username', flat=True)
    list = []
    for usr in usrs:
        list.append(usr)
    if request.method == 'POST':
        usr = request.POST['user']
        if User.objects.get(username = usr) is not None:
            user = User.objects.get(username = usr)
            if request.POST['action'] == 'auth':
                user.is_staff = True
                user.save()
            elif request.POST['action'] == 'susp':
                user.is_active = False
                user.save()
            elif request.POST['action'] == 'act':
                user.is_active = True
                user.save()
            return render_to_response('SecureWitness/auth.html',{'users' : list}, context)
        else:
            return render_to_response('SecureWitness/auth.html',{'users' : list}, context)

    return render_to_response('SecureWitness/auth.html',{'users' : list}, context)

@login_required
def group(request):
    context = RequestContext(request)
    grps = Group.objects.filter(users__username=request.user.username)
    usrs = User.objects.all()
    grps = grps.values_list('name', flat=True)
    usrs = usrs.values_list('username', flat=True)
    glist = []
    ulist = []#comment so the damn thing knows its changed
    for grp in grps:
        glist.append(grp)
    for usr in usrs:
        ulist.append(usr)
    if(request.method == 'POST'):
        if request.POST['action'] == 'newg' and request.POST['name'] is not None:
            dat = {'name' : request.POST['name'], 'users' : request.POST['user']}
            group_form = GroupForm(data=dat)
            if group_form.is_valid():
                new = group_form.save()
                new.save()
        elif request.POST['action'] == 'newu' and request.POST['grp'] is not None and request.POST['nusr'] is not None:
            group = Group.objects.get(name=request.POST['grp'])
            nuser = User.objects.get(username=request.POST['nusr'])
            if group is not None and nuser is not None:
                group.users.add(nuser)
                group.save()
    return render_to_response('SecureWitness/group.html',{'users' : ulist, 'groups' : glist}, context)

@login_required
def restricted(request):
    return HttpResponse("<a href='/SecureWitness/'>Index</a><br /> Since you're logged in, you can see this text!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/SecureWitness/')
