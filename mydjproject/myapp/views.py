from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
# Create your views here.

from . models import student
from . form import StudentForm


def home(request):
    return render(request,('home.html'))
def login(request):
    return render (request,('login.html'))
def addstudent(request):
    if request.method == "GET":
        context = {'form':StudentForm()}
        return render(request,'login.html',context)
    elif request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(addstudent)
        else:
            return render(request,'login.html',{'form':form})
def displayStudent(request):
    dbdata = student.objects.all()
    context = {'mydata':dbdata}
    return render(request,'demo.html',context)
def deletestudent(request,id):
    mydata = get_object_or_404(student,pk=id)
    mydata.delete()
    return redirect(displayStudent)