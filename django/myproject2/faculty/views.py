from django.shortcuts import render,HttpResponse,redirect
from faculty.forms import *
from  faculty.models import  *
from django.contrib import  messages
from django.core.mail import send_mail

from  faculty.models import  *

from myproject2 import settings
import random as rand
# Create your views here.
def index(req):
    return HttpResponse("hello")

def home(req):
    return render(req,'home.html')

def about(req):
    return render(req,"about.html")

def contact(req):
    if req.method=="POST":
        con=ContactForm(req.POST)
        if con.is_valid():
            con.save()
            messages.info(req,"data added succeess")
            return redirect('/faculty/data')
    form=ContactForm()

    return render(req,"contact.html",{'data':form})

def register(req):

    if req.method=="POST":
        con=FacultyRegistration(req.POST)
        if con.is_valid():
            con.save()
            return redirect('/faculty/home')
    

    reg=FacultyRegistration()

    return render(req,"register.html",{'form':reg})

def login(req):
    if req.method=="POST":
        user=Registration.objects.get(username=req.POST['uname'])
        print(user.username)
        if user.password==req.POST['psw']:
            return HttpResponse("LOGIN")
        return HttpResponse("invaild")
    return render(req,"login.html")
def data(req):
    data=Contact.objects.all()
    reg=Registration.objects.all()

    return render(req,"data.html",{'dis':data,'reg':reg})

def dele(req,id):
    d=Contact.objects.get(id=id)
    messages.warning(req,"{} data delete succeess".format(d.name))
    d.delete()

    return redirect('/faculty/data')
def update(req,id):
    data=Contact.objects.get(id=id)
    if req.method == "POST":
        up=ContactForm(req.POST,instance=data)
        if up.is_valid():
            up.save()
            messages.success(req,"{} data update succeess".format(data.name))

            return redirect('/faculty/data')
    up=ContactForm(instance=data)
    
    return render(req,"update.html",{"data":up})


def mail(req):
    if req.method=="POST":
        mail=req.POST['email']
        sub=req.POST['sub']
        mess=req.POST['me']
        df=settings.EMAIL_HOST_USER
        t=send_mail(sub,mess,df,[mail])
        if t==1:
            messages.success(req," mail succeess")
            return render(req,"mailsend.html")
            

    return render(req,"mailsend.html")


def img(req):
    if req.method=="POST":
        imgform=imgloadForm(req.POST,req.FILES)
        if imgform.is_valid():
            imgform.save()
            return redirect('/faculty/imgdisplay')

            

    imgform=imgloadForm()
    return render(req,'image.html',{'imform':imgform})

def imgdisplay(req):
    im=ImgLoad.objects.all()

    return render(req,'imgdisplay.html',{'img':im})


def emp(req,id):
    form=Emp(req.POST or None)
    eid=Registration.objects.get(id=id)
    if req.method == 'POST':
        if form.is_valid():
            data=form.save(commit=False)
            data.id=eid
            data.save()
            return redirect('/faculty/data')

    return render(req,'emp.html',{'form':form})