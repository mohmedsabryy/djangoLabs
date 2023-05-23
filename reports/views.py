from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect

# Create your views here.


def allstudents(req):
    return HttpResponseRedirect('/student')

def allstaff(req):
    return HttpResponseRedirect('/staff')

def mainreport(req):
    response_html_std = '<a href="http://127.0.0.1:8000/student/">All students</a>'
    response_html_staff = '<a href="http://127.0.0.1:8000/staff/">All Stuff</a>'
    res = HttpResponse(response_html_std)
    res.write('<br>'+'<br>'+response_html_staff)
    return res
