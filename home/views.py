

from django.shortcuts import render,redirect
from home.forms import studentsearchform,studentEditModelForm,studentcreateform
from home.models import Student,Library

from django.contrib import messages
# Create your views here.
def home_view(request):
	if request.method=='POST':
		search=studentsearchform(request.POST)
		# print(search)
		if search.is_valid():
			value = search.cleaned_data.get('q')
			result=Student.objects.filter(student_name__contains = value)
			return render(request,'search.html',{'result':result,'form':studentsearchform()})
	
	else:
		form=studentsearchform()
		result=Student.objects.all()
		return render(request,'search.html',{'form':form,'result':result})


def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def deletestudent(request,id):
	result=Student.objects.get(id=id)
	result.delete()
	messages.success(request,'delete sucessfully')
	return redirect('/')

def editstudent(request,id):
	student=Student.objects.get(id=id)
	if request.method=='POST':
		modelform=studentEditModelForm(request.POST,instance=student)
		if modelform.is_valid():
			modelform.save()
			return redirect('/')
	else:
		modelform=studentEditModelForm(instance=student)
		return render(request,'edit.html',{'form':modelform,'value':'Edit'})
		
		
def createstudent(request):
	if request.method=='POST':
		form=studentcreateform(request.POST)
		if form.is_valid():
			stud=Student.objects.create(student_name=form.cleaned_data.get('student_name'),
			department=form.cleaned_data.get('department'))
			stud.save()
			messages.success(request,"create sucessfully!!")
			return redirect('/')
	else:
		form=studentcreateform()
		return render(request,'create.html',{'form':form,'value':'Create'})