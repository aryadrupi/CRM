from django.shortcuts import render

from django.views import View

from .models import Payment,Transactions

import razorpay

from decouple import config

from django.db import transaction

# Create your views here.

class StudentPaymentView(View) :

    def get(self,request,*args,**kwargs):

        try:

            payment = Payment.objects.get(student__profile=request.user)

        except Payment.DoesNotExist:

            return render(request,'errorpages/pages-404.html')
        
        data = {'payment':payment}

        return render(request,'payments/student-payment-details.html',context=data)
    
class RazorPayView(View) :

    def get(self,request,*args,**kwargs):

        with transaction.atomic():

            payment_obj = Payment.objects.get(student__profile=request.user)

            amount = payment_obj.amount

            client = razorpay.Client(auth=(config('RZP_CLIENT_ID'),config('RZP_CLIENT_SECRET')))

            data = { "amount": amount * 100, "currency": "INR", "receipt": "order_rcptid_11" }

            payment = client.order.create(data=data) 

            order_id = payment.get('id')

            amount = payment.get('amount')

            Transactions.objects.create(payment=payment_obj,rzp_order_id=order_id,amount=amount)

            data = {'order_id':order_id,'amount':amount,'RZP_CLIENT_ID':config('RZP_CLIENT_ID')}

            return render(request,'payments/razorpay-page.html',context=data)