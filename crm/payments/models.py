from django.db import models

from student.models import BaseClass

class PaymentStatusChoice(models.TextChoices):

    PENDING = 'Pending','Pending'

    SUCCESS = 'Success','Success'

    FAILD = 'Failed','Failed'

class Payment(BaseClass):

    student = models.OneToOneField('student.Student',on_delete=models.CASCADE)

    amount = models.FloatField()

    status = models.CharField(max_length=20,choices=PaymentStatusChoice.choices,default=PaymentStatusChoice.PENDING)

    paid_at = models.DateTimeField(null=True,blank=True)

    def __str__(self):

        return f'{self.student.first_name}-{self.student.batch.name}'
    
    class Meta :

        verbose_name = 'Payments'

        verbose_name_plural = 'Payments'

class Transactions(BaseClass):

    payment = models.ForeignKey('Payment',on_delete=models.CASCADE)

    rzp_order_id = models.SlugField()

    amount = models.FloatField()

    status = models.CharField(max_length=20,choices=PaymentStatusChoice.choices,default=PaymentStatusChoice.PENDING)

    transaction_at = models.DateTimeField(null=True,blank=True)

    rzp_payment_id = models.SlugField(null=True,blank=True)

    rzp_signature = models.TextField(null=True,blank=True)

    def __str__(self):

        return f'{self.payment.student.first_name}-{self.payment.student.batch.name}{self.status}'
    
    class Meta :

        verbose_name = 'Transactions'

        verbose_name_plural = 'Transactions'


