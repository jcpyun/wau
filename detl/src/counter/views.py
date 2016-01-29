from django.shortcuts import render, get_object_or_404, render_to_response, RequestContext
from .models import click
from .forms import clickForm
##########
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect
from detl import settings
from django.contrib.auth.decorators import login_required
############
from django.contrib.auth.models import User
from .models import *



import datetime


# Create your views here.

class MyList(list):
    def last_index(self):
        return len(self)-1

    
def home(request):
    
    form=clickForm(request.POST or None)
    #print form
    if form.is_valid():
        save_it= form.save(commit=False)
        save_it.save()
    #instance= get_object_or_404(click, id=1)
    # instance= click.objects.get(id=1)
    queryset = click.objects.all()
    test = click.objects.all()
    yolo= test[:1]
    l= MyList(queryset)
    latest= queryset[l.last_index()].timestamp
    previous= queryset[l.last_index()-1].timestamp
    current= datetime.datetime.now()
    
    diff= current-latest
    min_sec= divmod(diff.days * 86400 + diff.seconds, 60)
    min_delt= min_sec[0]
    sec_delt= min_sec[1]
    wowtime= yolo[0].timestamp
    idtest= yolo[0].id
   
    #wowtime=l.last_index()[0].timestamp
    #print wowtime
    template= "home.html"
    context={
        "idtest": idtest,
        "current": current,
        "latest": latest,
        "previous": previous,
        "object_list": queryset,
        "cur": yolo[0],
        "min_sec": min_sec,
        "min_delt": min_delt,
        "sec_delt": sec_delt,
        
    }
    return render(request, template, context)