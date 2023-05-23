from django.urls import path
from . import views

urlpatterns = [
    path('allstudents', views.allstudents),
    path('allstuff', views.allstaff),
    path('mainreport', views.mainreport),

]