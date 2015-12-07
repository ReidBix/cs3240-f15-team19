# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from Project.SecureWitness.models import *
from Project.SecureWitness.forms import *
from django.shortcuts import redirect, get_object_or_404

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
import pdb
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

@login_required
def add_folder(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = folderForm(request.POST)
        print(request.POST['title'])
        if form.is_valid():
            form.save()
            the_folders = Folder.objects.all()
            print(len(the_folders))
            return index(request)
        else:
            print(form.errors)
    else:
        form = folderForm()

    the_folders = Folder.objects.all()
    if(len(the_folders) == 0):
    	print(len(the_folders))

    return render_to_response('SecureWitness/addFolder.html', {'folders': the_folders, 'form': form}, context)



# def list(request):
#    # pdb.set_trace()
#     # Handle file upload
#
#     if request.method == 'POST':
#         print(len(request.FILES.getlist('img')))
#         encrypted2 = False
#         private2 = False
#         timestamp2 = datetime.now()
#         if 'encrypted' in request.POST:
#                 encrypted2 = True
#         if 'private' in request.POST:
#                 private2 = True
#         form = ReportForm(request.POST, request.FILES)
#         if form.is_valid():
#             newdoc = Report(user = request.user, docfile = request.FILES['docfile'],
#                               title = request.POST['title'], description = request.POST['description'],
#                               detailed_description = request.POST['detailed_description'],
#                               encrypted = encrypted2, private = private2, timestamp = timestamp2)
#
#             newdoc.save()
# 		#used to be newdoc.save()
#             # Redirect to the document list after POST
#             return HttpResponseRedirect(reverse('Project.SecureWitness.views.list'))
#     else:
#         form = ReportForm() # A empty, unbound form
#
#     squad = Report.objects.filter(encrypted=True)
#     # Load documents for the list page
#     squad_again = ""
#     user2 = request.user
#     if str(user2) != 'admin':
#     	squad_again = Report.objects.filter(user=user2)
#     else:
#     	squad_again = Report.objects.all()
# # Render list page with the documents and the form
#     return render_to_response(
#         'SecureWitness/list.html',
#         {'documents': squad_again, 'form': form},
#         context_instance=RequestContext(request)
#     )

@login_required
def reports(request, rep_id):
    if request.method == 'POST':
        report = get_object_or_404(Report, pk=rep_id)
        report.delete()

    reporter_name = get_object_or_404(User, username = request.user)
    report_list = Report.objects.filter(user = reporter_name).order_by('timestamp')
    return render(request, 'SecureWitness/reports.html', {'reports': report_list})

@login_required
def disp_report(request, rep_id):
    report = get_object_or_404(Report, pk=rep_id)
    files = Upload.objects.filter(report=report)
    return render_to_response('SecureWitness/disp_report.html',{'report': report, 'files':files}, context_instance=RequestContext(request))

@login_required
def edit_report(request, id):
    old_report = get_object_or_404(Report, pk=id)


    if request.method == 'POST':

        report_form = ReportForm(request.POST, request.FILES,instance=old_report)
        upload_form = UploadForm(request.POST, request.FILES)
        if report_form.is_valid and upload_form.is_valid():
            nrep = report_form.save()
            upload = upload_form.save(commit=False)
            upload.name = request.FILES
            upload.report = nrep
            upload.save()

            return redirect('/SecureWitness/reports/')

    else:
        report_form = ReportForm(instance=old_report)
        upload_form = UploadForm()

    context = {'report_form': report_form, 'upload_form': upload_form, 'report': old_report}
    return render(request, 'SecureWitness/edit_report.html', context)


@login_required
def add_report(request):

    if request.method == 'POST':

        report_form = ReportForm(request.POST, request.FILES)
        upload_form = UploadForm(request.POST, request.FILES)

        if report_form.is_valid() and upload_form.is_valid():
            # file is saved
            reporter = get_object_or_404(User, username = request.user)
            nreport = report_form.save(commit=False)
            nreport.user = reporter
            nreport.timestamp = datetime.now()
            nreport.save()

            upload = upload_form.save(commit=False)
            upload.name = request.FILES['file']
            upload.report = nreport
            upload.save()


            return redirect('/SecureWitness/reports/')
        else:
            print(report_form.errors, upload_form.errors)
    else:
        report_form = ReportForm()
        upload_form = UploadForm()
        print(request.user)
    return render_to_response('SecureWitness/add_report.html', {'report_form': report_form, 'upload_form': upload_form},context_instance=RequestContext(request))

def register(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        mutable = request.POST._mutable
        request.POST._mutable = True
        request.POST['tempprivate'] = ''
        request.POST._mutable = mutable
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
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
    the_folders = Folder.objects.all()
    return render_to_response(
        'SecureWitness/register.html',
        {'folders': the_folders, 'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
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

@login_required
def search(request):

    if request.GET:
        form = ReportSearchForm(request.GET)
        if form.is_valid():
            results = form.get_result_queryset()
        else:
            results = []
    else:
        form = ReportSearchForm()
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
    if request.method == 'POST':
        usr = request.POST['user']
        if User.objects.get(username = usr) is not None:
            user = User.objects.get(username = usr)
            user.is_staff = True
            user.save()
            return HttpResponseRedirect('/SecureWitness/auth/')
        else:
            return HttpResponseRedirect('/SecureWitness/auth/')

    return render_to_response('SecureWitness/auth.html', {}, context)

@login_required
def groups(request):
    if request.method == 'POST':
        current_user = request.user
        groupname = request.POST['groupname']
        form = GroupForm(request.POST)
        #Check if exists
        group = Group.objects.get_or_create(name=groupname)
        # Already exists
        if(group[1] == False):
            g = Group.objects.get(name=groupname)
            #Check if user is a part of group
            #Doesn't belong to group
            if (not current_user.is_staff):
                if (not g in current_user.groups.all()):
                    return HttpResponse("You don't belong to this group.")
        # Doesn't exist
        elif (group[1] ==True):
            g = Group.objects.get(name=groupname)
            g.user_set.add(current_user)
        grouplist = Group.objects.all()

        if form.is_valid():
            g = Group.objects.get(name=groupname)
            if (group[1] == False):
                # Check if user is a part of group
                # Doesn't belong to group
                if (not current_user.is_staff):
                    # Can edit any group
                    if (g in current_user.groups.all()):
                        pass
                    # Can't edit any group
                    if (not g in current_user.groups.all()):
                        return HttpResponse("You don't belong to this group.")
                # Does belong to group
                u = form.cleaned_data['user']
                if (not form is None):
                    if(User.objects.filter(username=u).exists()):
                        g.user_set.add(u)
            # Doesn't exist
            elif (group[1] == True):
                u = form.cleaned_data['user']
                if (not form is None):
                    if (User.objects.filter(username=u).exists()):
                        g.user_set.add(u)
            #If user add is blank
            return HttpResponseRedirect('/SecureWitness/groups/')
    else:
        form = GroupForm()
        grouplist = Group.objects.all()
    return render_to_response('SecureWitness/groups.html',
                                  RequestContext(request, {
                                      'form': form,
                                      'grouplist': grouplist,
                                  }))


@login_required
def restricted(request):
    return HttpResponse("<a href='/SecureWitness/'>Index</a><br /> Since you're logged in, you can see this text!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/SecureWitness/')
