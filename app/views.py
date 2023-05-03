from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

from app.models import *

from app.forms import *

def registration(request):
    UFD=UserForm()
    PFD=ProfileForm()
    d={'UFD':UFD,'PFD':PFD}

    if request.method=='POST' and request.FILES:
        UFD=UserForm(request.POST)
        PFD=ProfileForm(request.POST,request.FILES)
        if UFD.is_valid() and PFD.is_valid():
            NSUO=UFD.save(commit=False)
            password=UFD.cleaned_data['password']
            NSUO.set_password(password)
            NSUO.save()


            NSPO=PFD.save(commit=False)
            NSPO.username=NSUO
            NSPO.save()
            return HttpResponse('Registration is successfull')
        else:
            return HttpResponse('Not Valid')

    return render(request,'registration.html',d)