from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Student
from staff.models import Staff

# Create your views here.


def all_std(req):
    students = Student.objects.all()
    return render(req, 'student/std_list.html', {'students': students})

def insert(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        age = req.POST.get('age')
        city = req.POST.get('city')
        supervisor_id = req.POST.get('supervisor')
        supervisor = Staff.objects.get(id=supervisor_id)
        student = Student(name=name, age=age, city=city, supervisor=supervisor)
        student.save()
        return redirect('/student/')
    supervisors = Staff.objects.all()
    return render(req, 'student/std_insert.html',{'supervisors': supervisors})

def update(req,std_id):
    student = get_object_or_404(Student, id=std_id)
    if req.method == 'POST':
        name = req.POST.get('name')
        age = req.POST.get('age')
        city = req.POST.get('city')
        supervisor_id = req.POST.get('supervisor')
        supervisor = Staff.objects.get(id=supervisor_id)
        student.name = name
        student.age = age
        student.city = city
        student.supervisor = supervisor
        student.save()
        return redirect('/student/')

    supervisors = Staff.objects.all()
    return render(req, 'student/std_update.html', {'student': student, 'supervisors': supervisors})



def delete(req,std_id):
    student = get_object_or_404(Student, id=std_id)
    student.delete()
    return redirect('/student/')
