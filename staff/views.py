from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Staff

# Create your views here.

def all_staff(req):
    sups = Staff.objects.all()
    return render(req, 'staff/staff_list.html', {'sups': sups})

def insert(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        sup = Staff(name=name)
        sup.save()
        return redirect('/staff/')
    return render(req, 'staff/staff_insert.html')

def update(req,sup_id):
    sup = get_object_or_404(Staff, id=sup_id)
    if req.method == 'POST':
        name = req.POST.get('name')
        sup.name = name
        sup.save()
        return redirect('/staff/')

    return render(req, 'staff/staff_update.html', {'sup': sup})



def delete(req,sup_id):
    sup = get_object_or_404(Staff, id=sup_id)
    sup.delete()
    return redirect('/staff/')
