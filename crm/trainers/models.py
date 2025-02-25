from django.db import models

from student.models import BaseClass,DistrictView

# Create your models here.

class Trainers(BaseClass):

    first_name = models.CharField(max_length=25)

    last_name = models.CharField(max_length=25)

    employee_id = models.CharField(max_length=10)

    photo = models.ImageField(upload_to='trainers')

    email = models.EmailField()

    contact = models.CharField(max_length=12)

    house_name = models.CharField(max_length=25)

    post_office = models.CharField(max_length=25)

    district = models.CharField(max_length=20,choices=DistrictView.choices)

    pincode = models.CharField(max_length=6)

    qualification = models.CharField(max_length=20)
    
    stream = models.CharField(max_length=25)

    id_card = models.FileField(upload_to='trainers/idproof')

    course = models.ForeignKey('courses.Courses',null=True,on_delete=models.SET_NULL)

    def __str__(self):

        return f'{self.first_name}-{self.last_name}'
    
    class Meta:

        verbose_name = 'Trainers'

        verbose_name_plural ='Trainers'