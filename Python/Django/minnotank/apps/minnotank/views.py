# from __future__ import unicode_literals
# from django.shortcuts import render, HttpResponse, redirect, reverse
# from google.oauth2 import id_token
# from google.auth.transport import requests

# from google.oauth2.credentials import Credentials
# from google.auth.transport.requests import AuthorizedSession
# import json
# from .models import User, Startup, StartupImage, Upvote, StartupMedia
# import re
# from django.contrib import messages

# from django.core.serializers.json import DjangoJSONEncoder
# from django.core.serializers import serialize

# ###################################

# def createJobFromStartUp (request,comp_id):
#     errors = Job.objects.SUJobManager(request.POST)
#     if len(errors):
#         for mess in errors.values():
#             messages.error(request, mess)
#         return redirect('minno:newJob')

#     newSUJob = Job.objects.create(
#         company_name = Startup.objects.get(id = comp_id).title, 
#         title = request.POST['title'], 
#         location = request.POST['location'], 
#         desc = request.POST['desc'], 
#         link = request.POST['link'], 
#         icon = Startup.objects.get(id = comp_id).icon, 
#         user = User.objects.get(id = request.session["id"]),
#         startup = Startup.objects.get(id = comp_id)
#         )

#     newSUJob.owners.add(User.objects.get(id = request.session['id'])) 
#     return redirect('minno:feed')

# def createJobFromUser (request):
#     errors = Job.objects.JobManager(request.POST)
#     errors = Startup.objects.size(request.FILES, ICON_SIZE, 'icon')
#     if len(errors):
#         for mess in errors.values():
#             messages.error(request, mess)
#         return redirect('minno:newJob')

#     newUJob = Job.objects.create(
#         company_name = request.POST['company_name'], 
#         title = request.POST['title'], 
#         location = request.POST['location'], 
#         desc = request.POST['desc'], 
#         link = request.POST['link'], 
#         icon = request.FILES['icon'], 
#         user = User.objects.get(id = request.session["id"]),
#         )

#     newUJob.owners.add(User.objects.get(id = request.session['id']))
#     return redirect('minno:feed')

# ###################################

# def createDealFromStartUp (request, comp_id):
#     errors = Deal.objects.SUDealManager(request.POST)
#     if len(errors):
#         for mess in errors.values():
#             messages.error(request, mess)
#         return redirect('minno:newJob')

#     newSUDeal = Deal.objects.create(
#         company_name = Startup.objects.get(id = comp_id).title, 
#         deal_name = request.POST['deal_name'], 
#         value = request.POST['value'], 
#         desc = request.POST['desc'], 
#         link = request.POST['link'], 
#         icon = Startup.objects.get(id = comp_id).icon, 
#         user = User.objects.get(id = request.session["id"]),
#         startup = Startup.objects.get(id = comp_id)
#     )

#     newSUDeal.owners.add(User.objects.get(id = request.session['id']))
#     return redirect('minno:feed')

# def createDealFromUser (request):
#     errors = Deal.objects.DealManager(request.POST)
#     errors = Startup.objects.size(request.FILES, ICON_SIZE, 'icon')
#     if len(errors):
#         for mess in errors.values():
#             messages.error(request, mess)
#         return redirect('minno:newJob')

#     newUDeal = Deal.objects.create(
#         company_name = request.POST['company_name'], 
#         deal_name = request.POST['deal_name'], 
#         value = request.POST['value'], 
#         desc = request.POST['desc'], 
#         link = request.POST['link'], 
#         icon = request.FILES['icon'],
#         user = User.objects.get(id = request.session["id"]),
#     )

#     newUDeal.owners.add(User.objects.get(id = request.session['id']))
#     return redirect('minno:feed')

# ###################################

# def editJobStartUp(request, id):
#     context = {
#         'editJobStartUp' : Job.objects.get(id=id)
#     }
#     return render(request,'editJobStartUp.html', context)

# def updateJobStartUp(request, id):
#     errors = Job.objects.SUJobManager(request.POST)
#     if len(errors):
#         for mess in errors.values():
#             messages.error(request, mess)
#         return redirect('minno:updateJobSU')

#     updateJSU = Job.objects.get(id= id)
#     updateJSU.title = request.POST['title']
#     updateJSU.location = request.POST['location']
#     updateJSU.desc = request.POST['desc']
#     updateJSU.link = request.POST['link']
#     updateJSU.save()

#     return redirect('minno:feed')

# ###################################

# def editJobUser(request, id):
#     context = {
#         'editJobUser' : Job.objects.get(id=id)
#     }
#     return render(request,'editJobUser.html', context)

# def updateJobUser(request, id):
#     errors = Job.objects.JobManager(request.POST)
#     errors = Startup.objects.size(request.FILES, ICON_SIZE, 'icon')
#     if len(errors):
#         for mess in errors.values():
#             messages.error(request, mess)
#         return redirect('minno:updateJobU')

#     updateJU = Job.objects.get(id=id)
#     updateJU.company_name = request.POST['company_name']
#     updateJU.title = request.POST['title']
#     updateJU.location = request.POST['location']
#     updateJU.desc = request.POST['desc']
#     updateJU.link = request.POST['link']
#     updateJU.icon = request.POST['icon']
#     updateJU.save()

#     return redirect('minno:feed')

# ###################################

# def editDealStartUp(request, id):
#     context = {
#         'editDealSU' : Deal.objects.get(id=id)
#     }
#     return render(request,'editDealSU.html', context)

# def updateDealStartUp (request, id):
#     errors = Deal.objects.SUDealManager(request.POST)
#     if len(errors):
#         for mess in errors.values():
#             messages.error(request, mess)
#         return redirect('minno:editDealSU')

#     updateDealSU = Deal.objects.get(id=id)
#     updateDealSU.deal_name = request.POST['deal_name']
#     updateDealSU.value = request.POST['value']
#     updateDealSU.desc = request.POST['desc']
#     updateDealSU.link = request.POST['link']
#     updateDealSU.save()

#     return redirect('minno:feed')

# ###################################

# def editDealUser (request, id):
#     context = {
#         'editDealUser' : Deal.objects.get(id=id)
#     }
#     return render(request,'editDealUser.html', context)

# def updateDealUser (request, id):
#     errors = Deal.objects.DealManager(request.POST)
#     if len(errors):
#         for mess in errors.values():
#             messages.error(request, mess)
#         return redirect('minno:editDealUser')

#     updateDealU = Deal.objects.get(id=id)
#     updateDealU.deal_name = request.POST['deal_name']
#     updateDealU.value = request.POST['value']
#     updateDealU.desc = request.POST['desc']
#     updateDealU.link = request.POST['link']
#     updateDealU.save()

#     return redirect('minno:feed')

# ###################################

# def deleteJobSU (request, id):
#     if "user_id" not in request.session:
#         return redirect ('/')
#     userjobs = Job.objects.filter(user = User.objects.get(id = request.session["id"]))
#     for job in userjobs:
#         if(job.id == id):
#             jobSU= Job.objects.get(id=id)
#             jobSU.delete()
#             return redirect('/dashboard')
#         messages.error(request, 'Only the job creator can delete this job.')
#         return redirect('/')   

# def deleteJobUser (request, id):
#     if "user_id" not in request.session:
#         return redirect ('/')
#     userjobs = Job.objects.filter(user = User.objects.get(id = request.session["id"]))
#     for job in userjobs:
#         if(job.id == id):
#             jobU= Job.objects.get(id=id)
#             jobU.delete()
#             return redirect('/dashboard')
#         messages.error(request, 'Only the job creator can delete this job.')
#         return redirect('/')   

# ###################################

# def deleteDealSU (request, id):
#     if "user_id" not in request.session:
#         return redirect ('/')
#     userdeals = Deal.objects.filter(user = User.objects.get(id = request.session["id"]))
#     for deal in userdeals:
#         if(deal.id == id):
#             dealSU= Deal.objects.get(id=id)
#             dealSU.delete()
#             return redirect('/dashboard')
#         messages.error(request, 'Only the deal creator can delete this deal.')
#         return redirect('/')

# def deleteDealUser (request, id):
#     if "user_id" not in request.session:
#         return redirect ('/')
#     userdeals = Deal.objects.filter(user = User.objects.get(id = request.session["id"]))
#     for deal in userdeals:
#         if(deal.id == id):
#             dealU= Deal.objects.get(id=id)
#             dealU.delete()
#             return redirect('/dashboard')
#         messages.error(request, 'Only the deal creator can delete this deal.')
#         return redirect('/')

# ###################################

















from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect, reverse
from google.oauth2 import id_token
from google.auth.transport import requests

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import AuthorizedSession
import json
from .models import *
import re
from django.contrib import messages

from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize

###################################

def sessionJobStartUp (request,comp_id):
    errors = Job.objects.SUJobManager(request.POST)
    if len(errors):
        return HttpResponse(json.dumps({'errors':errors}), content_type='application/json')

    request.session['company_name'] = Startup.objects.get(id = comp_id).title
    request.session['title'] = request.POST['title']
    request.session['location'] = request.POST['location']
    request.session['desc'] = request.POST['desc']
    request.session['link'] = request.POST['link']
    request.session['icon'] = Startup.objects.get(id = comp_id).icon
    request.session['user'] = User.objects.get(id = request.session["id"])
    request.session['startup'] = Startup.objects.get(id = comp_id)
 
    return HttpResponse(content_type='application/json')

def sessionJobUser (request):
    errors = Job.objects.JobManager(request.POST)
    if len(errors):
        return HttpResponse(json.dumps({'errors':errors}), content_type='application/json')
    errors = Startup.objects.size(request.FILES, ICON_SIZE, 'icon')
    if len(errors):
        return HttpResponse(json.dumps({'errors':errors}), content_type='application/json')

    request.session['company_name'] = request.POST['company_name'] 
    request.session['title'] = request.POST['title']
    request.session['location'] = request.POST['location'] 
    request.session['desc'] = request.POST['desc']
    request.session['link'] = request.POST['link'] 
    request.session['icon'] = request.FILES['icon']
    request.session['user'] = User.objects.get(id = request.session["id"])

    return HttpResponse(content_type='application/json')

###################################

def sessionDealStartUp (request, comp_id):
    errors = Deal.objects.SUDealManager(request.POST)
    if len(errors):
        return HttpResponse(json.dumps({'errors':errors}), content_type='application/json')

    request.session['company_name'] = Startup.objects.get(id = comp_id).title
    request.session['deal_name'] = request.POST['deal_name']
    request.session['value'] = request.POST['value']
    request.session['desc'] = request.POST['desc']
    request.session['link'] = request.POST['link']
    request.session['icon'] = Startup.objects.get(id = comp_id).icon
    request.session['user'] = User.objects.get(id = request.session["id"])
    request.session['startup'] = Startup.objects.get(id = comp_id)

    return HttpResponse(content_type='application/json')

def sessionDealUser (request):
    errors = Deal.objects.DealManager(request.POST)
    if len(errors):
        return HttpResponse(json.dumps({'errors':errors}), content_type='application/json')
    errors = Startup.objects.size(request.FILES, ICON_SIZE, 'icon')
    if len(errors):
        return HttpResponse(json.dumps({'errors':errors}), content_type='application/json')

    request.session['company_name'] = request.POST['company_name']
    request.session['deal_name'] = request.POST['deal_name']
    request.session['value'] = request.POST['value']
    request.session['desc'] = request.POST['desc']
    request.session['link'] = request.POST['link'] 
    request.session['icon'] = request.FILES['icon']
    request.session['user'] = User.objects.get(id = request.session["id"]),
    
    return HttpResponse(content_type='application/json')

###################################


def updateJobStartUp(request, id):
    errors = Job.objects.SUJobManager(request.POST)
    if len(errors):
        return HttpResponse(json.dumps({'errors':errors}), content_type='application/json')

    updateJSU = Job.objects.get(id= id)
    updateJSU.title = request.POST['title']
    updateJSU.location = request.POST['location']
    updateJSU.desc = request.POST['desc']
    updateJSU.link = request.POST['link']
    updateJSU.save()

    return HttpResponse(json.dumps({'success': 1, 'job':updateJSU.id}), content_type='application/json')

###################################

def updateJobUser(request, id):
    errors = Job.objects.JobManager(request.POST)
    if len(errors):
        return HttpResponse(json.dumps({'errors':errors}), content_type='application/json')
    errors = Startup.objects.size(request.FILES, ICON_SIZE, 'icon')
    if len(errors):
        return HttpResponse(json.dumps({'errors':errors}), content_type='application/json')

    updateJU = Job.objects.get(id=id)
    updateJU.company_name = request.POST['company_name']
    updateJU.title = request.POST['title']
    updateJU.location = request.POST['location']
    updateJU.desc = request.POST['desc']
    updateJU.link = request.POST['link']
    updateJU.icon = request.POST['icon']
    updateJU.save()

    return HttpResponse(json.dumps({'success': 1, 'job':updateJU.id}), content_type='application/json')

###################################

def updateDealStartUp (request, id):
    errors = Deal.objects.SUDealManager(request.POST)
    if len(errors):
        return HttpResponse(json.dumps({'errors':errors}), content_type='application/json')

    updateDealSU = Deal.objects.get(id=id)
    updateDealSU.deal_name = request.POST['deal_name']
    updateDealSU.value = request.POST['value']
    updateDealSU.desc = request.POST['desc']
    updateDealSU.link = request.POST['link']
    updateDealSU.save()

    return HttpResponse(json.dumps({'success': 1, 'deal':updateDealSU.id}), content_type='application/json')

###################################

def updateDealUser (request, id):
    errors = Deal.objects.DealManager(request.POST)
    if len(errors):
        return HttpResponse(json.dumps({'errors':errors}), content_type='application/json') 

    updateDealU = Deal.objects.get(id=id)
    updateDealU.deal_name = request.POST['deal_name']
    updateDealU.value = request.POST['value']
    updateDealU.desc = request.POST['desc']
    updateDealU.link = request.POST['link']
    updateDealU.save()

    return HttpResponse(json.dumps({'success': 1, 'job':newSUJob.id}), content_type='application/json')

################################### 

def deleteJob (request, id):
    if "user_id" not in request.session:
        return reset(request)
    userjobs = Job.objects.filter(user = User.objects.get(id = request.session["id"]))
    for job in userjobs:
        if(job.id == id):
            jobU= Job.objects.get(id=id)
            jobU.delete()
            return HttpResponse(content_type='application/json')
        errors = 'Only the job creator can delete this job.'
        return HttpResponse(json.dumps({'errors':errors}), content_type='application/json')  

###################################

def deleteDeal (request, id):
    if "user_id" not in request.session:
        return reset(request)
    userdeals = Deal.objects.filter(user = User.objects.get(id = request.session["id"]))
    for deal in userdeals:
        if(deal.id == id):
            dealU= Deal.objects.get(id=id)
            dealU.delete()
            return HttpResponse(content_type='application/json')
        errors = 'Only the deal creator can delete this deal.'
        return HttpResponse(json.dumps({'errors':errors}), content_type='application/json')

###################################