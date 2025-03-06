from django.db import models

# Create your models here.

from student.models import BaseClass

class PaymentSettlechoices(models.TextChoices):

    ONE_TIME = 'ONE_TIME','ONE_TIME'

    INSTALLMENTS = 'INSTALLMENTS','INSTALLMENTS'

class InstallmentChoices(models.IntegerChoices):

    TWO = 2,'2'

    THREE = 3,'3'

    FOUR = 4,'4'

    FIVE = 5,'5'

    SIX = 6,'6'

class PaymentStructure(BaseClass) :

    student = models.OneToOneField('student.Student',on_delete=models.CASCADE)

    one_time_or_installments = models.CharField(max_length=20,choices=PaymentSettlechoices.choices)

    no_of_installments = models.IntegerField(choices=InstallmentChoices.choices,null=True,blank=True)

    fee_to_be_paid = models.FloatField()

    def __str__(self) :

        return f'{self.student.first_name} {self.student.batch.name} Payment Structure'
    
    class Meta :

         verbose_name = 'Payment Structure'

         verbose_name_plural = 'Payment Structure'

         ordering = ['id']


