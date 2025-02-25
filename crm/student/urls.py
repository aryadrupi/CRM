from django.urls import path

from . import views

urlpatterns = [

    path('dashboard/', views.Dashboardview.as_view(),name = 'dashboard'),

    path('students/', views.StudentListview.as_view(),name = 'students'),

    path('form/', views.FormView.as_view(),name = 'form'),

    path('student-detail/<str:uuid>/',views.StudentDetailView.as_view(),name = 'student-detail'),

    path('delete/<str:uuid>/',views.StudentDeleteView.as_view(),name = 'delete'),
    
    path('student-update/<str:uuid>/',views.StudentUpdateView.as_view(),name = 'student-update')

]
