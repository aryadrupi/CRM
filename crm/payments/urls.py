from django.urls import path

from .import views

urlpatterns =[

    path('student-payment-details/',views.StudentPaymentView.as_view(),name='student-payment-details'),
    path('Razorpay-view/',views.RazorPayView.as_view(),name='Razorpay-view'),
    
]
