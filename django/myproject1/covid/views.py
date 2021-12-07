from django.shortcuts import render,redirect
from  django.http import HttpResponse
from covid.models import *


# Create your views here.
def home(req):
    data={'name':'pavan','age':21}
    #return HttpResponse("<h1>Welcome pavan this u r 1st django project</h1>")
    return render(req,"start\home.html",{"info":data})

def about(request):
    return render(request,'about.html')
def tom(request):
    return render(request,"start\pj.html")

def reg(req):
    if req.method=='POST':
        name=req.POST['pname']
        
        age=req.POST['age']
        email= req.POST['email']
        
        data=Patients.objects.create(p_name=name,p_age=age,p_email=email)
        return HttpResponse('data stored entered')
    return render(req,'reg.html')

def student_reg(req):
   
    if req.method=='POST':
        
        s_name= req.POST['s_name']
        s_age= req.POST['s_age']
        s_phone=req.POST['s_phone']
        s_email=req.POST['s_email']
        s_gender= req.POST['gender']
        s_add= req.POST['s_add']
        s_uname=req.POST['s_uname']
        s_pass= req.POST['s_pass']
        s_rollno= req.POST['s_roll']
        data=student.objects.create(s_name=s_name,s_age=s_age, s_phone=s_phone, s_email=s_email, s_gender=s_gender,s_rollno=s_rollno, s_add=s_add,s_uname=s_uname,s_pass=s_pass)
        return render(req,'student_registration.html',{'reg':True})

    return render(req,'student_registration.html',{'reg':False})

def display(req):

    data=student.objects.all()
    return render(req,'display.html',{'info':data})

def edit(req,id):
    data= student.objects.get(id=id)

    return render(req,'edit.html',{'data':data})
def update(req,id):
    if req.method=='POST':
        name=req.POST['name']
        age= req.POST['age']
        email=req.POST['email']
        data= student.objects.filter(id=id).update(s_name=name,s_age=age,s_email=email)
        return redirect('/display')

    return render(req,'edit.html')

def deld(req,id):
    data=student.objects.get(id=id)
    data.delete()
    return redirect('/display')
