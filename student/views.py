from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Students
from django.contrib.auth.models import User, auth
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def addstudent(request):
    if request.method == 'POST':
        name = request.POST['name']
        roll = request.POST['roll']
        Gender = request.POST['gender']
        division = request.POST['div']
        year = request.POST['year']
        branch = request.POST['branch']
        dob = request.POST['dob']
        prn = request.POST['prn']
        email = request.POST['email']
        contact = request.POST['contact']
        address = request.POST['address']
        student=Students.objects.create(name=name,roll=roll,Gender=Gender,division=division,year=year,branch=branch,dob=dob,prn=prn,email=email,contact=contact,address=address)
        student.save()
    messages.info(request,"Information saved")
    return render(request, 'addstudent.html')


def displaystudent(request):
    cards=Students.objects.all()
    context={'cards' : cards}
    return render(request,'displaystudent.html',context)

def updatestudent(request):
    if request.method == 'POST':
        DEL = request.POST['id']
        Students.objects.filter(id=DEL).delete()
    cards=Students.objects.all()
    context={'cards' : cards}
    return render(request,'updatestudent.html',context)


def updstd(request):
    if request.method == 'POST':
        upd = request.POST['id']
        name = request.POST['name']
        roll = request.POST['roll']
        Gender = request.POST['gender']
        division = request.POST['div']
        year = request.POST['year']
        branch = request.POST['branch']
        dob = request.POST['dob']
        prn = request.POST['prn']
        email = request.POST['email']
        contact = request.POST['contact']
        address = request.POST['address']
        s=Students.objects.filter(id=upd).update(name=name,roll=roll,Gender=Gender,division=division,year=year,branch=branch,dob=dob,prn=prn,email=email,contact=contact,address=address)
        print(s)
    return render(request,'updstd.html')