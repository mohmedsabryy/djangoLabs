from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_std, name="all_std"),
    path('insert/', views.insert),
    path('update/<int:std_id>/', views.update, name='update_student'),
    path('delete/<int:std_id>/', views.delete, name='delete_student')
]