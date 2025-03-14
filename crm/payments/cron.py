from .models import Payment

from django.utils import timezone

import threading

from student.utility import send_email

from apscheduler.schedulers.background import BackgroundScheduler

# cron to sent reminder email about payment

def reminder_email():

    current_date = timezone.now().date()

    five_days_before_data = current_date - timezone.timedelta(days=5)

    pending_payments = Payment.objects.filter(status='Pending',student__join_date__lte=five_days_before_data)

    if pending_payments.exists():

        # sending payment remainder to student through mail

        for payment in pending_payments:

            subject = 'Payment Remainder'

            recipients = [payment.student.email]

            template = 'email/payment-reminder.html'

            context = {'name':f'{payment.student.first_name} {payment.student.last_name}'}

            # send_email(subject,recipients,template,context)

            thread = threading.Thread(target=send_email,args=(subject,recipients,template,context))

            thread.start()

        print('all mail sent')

# apsheduler  (advanced python sheduler)

def sheduler_start() :

    scheduler = BackgroundScheduler()

    scheduler.add_job(reminder_email,'cron',hour=10,minute=0)

    scheduler.start()


    
