from django.db import models

import uuid

# Create your models here.

class BaseClass(models.Model) :

    uuid = models.SlugField(unique = True,default = uuid.uuid4)

    active_status = models.BooleanField(default = True)

    created_at = models.DateTimeField(auto_now_add = True)

    updated_at = models.DateTimeField(auto_now = True)

    class Meta :

        abstract = True

class CourseChoices(models.TextChoices) :

    # variable = databasevalue , representation

    PY_DJANGO = 'PY-DJANGO','PY-DJANGO'

    MEARN = 'MEARN','MEARN'

    DATA_SCIENCE = 'DATA_SCIENCE','DATA_SCIENCE'

    SOFTWARE_TESTING = 'SOFTWARE_TESTING','SOFTWARE_TESTING'

class DistrictView(models.TextChoices) :

    TRIVANDRUM = 'TRIVANDRUM','TRIVANDRUM'

    KOLLAM = 'KOLLAM','KOLLAM'

    PATHANAMTHITTA = 'PATHANAMTHITTA','PATHANAMTHITTA'

    ALAPPUZHA = 'ALAPPUZHA','ALAPPUZHA'

    KOTTAYAM = 'KOTTAYAM','KOTTAYAM'

    IDUKKI = 'IDUKKI','IDUKKI'

    ERNAKULAM = 'ERNAKULAM','ERNAKULAM'

    TRISSUR = 'TRISSUR','TRISSUR'

    PALAKKAD = 'PALAKKAD','PALAKKAD'

    MALAPPURAM = 'MALAPPURAM','MALAPPURAM'

    KOZHIKODE = 'KOZHIKODE','KOZHIKODE'

    WAYANAD = 'WAYANAD','WAYANAD'

    KANNUR = 'KANNUR','KANNUR'

    KASARKODE = 'KASARKODE','KASARKODE'

class BatchView(models.TextChoices) :

    PY_NOV_2024 = 'PY_NOV_2024','PY_NOV_2024'

    PY_Jan_2025 = 'PY_Jan_2025','PY_Jan_2025'

    DS_JAN_2025 = 'DS_JAN_2025','DS_JAN_2025'

    ST_JAN_2025 = 'ST_JAN_2025','ST_JAN_2025'

    MEARN_Jan_2025 = 'MEARN_Jan_2025','MEARN_Jan_2025'

    MEARN_JAN_2024 = 'MEARN_JAN_2024','MEARN_JAN_2024'

class TrainerView(models.TextChoices) :

    JOHN_DOE = 'JOHN_DOE','JOHN_DOE'

    JAMES = 'JAMES','JAMES'

    PETER = 'PETER','PETER'

    ALEX = 'ALEX','ALEX'

# class Student(models.Model) :
class Student(BaseClass) :

    ''' personal details fields '''

    profile = models.OneToOneField('authentication.Profile',on_delete = models.CASCADE)

    first_name = models.CharField(max_length = 50)

    last_name = models.CharField(max_length = 50)

    photo = models.ImageField(upload_to = 'students')

    email = models.EmailField(unique = True)

    contact_num = models.CharField(max_length = 50)

    house_name = models.TextField()

    post_office = models.CharField(max_length = 50)

    district = models.CharField(max_length = 50,choices = DistrictView.choices)

    pincode = models.CharField(max_length = 6)


    ''' course details fields '''


    adm_number = models.CharField(max_length = 50)

    # course = models.CharField(max_length = 50,choices = CourseChoices.choices)  # Python Django , Mearn , ST , DS 

    # batch = models.CharField(max_length = 50,choices=BatchView.choices)   # PY-NOV-2024,PY-Jan-2025,DS-JAN-2025,MEARN-Jan-2025,MEARN-JAN-2024,ST-JAN-2025

    course = models.ForeignKey('courses.Courses',null=True,on_delete = models.SET_NULL)

    # batch_date = models.DateField()

    batch = models.ForeignKey('batches.Batches',null=True,on_delete = models.SET_NULL)

    join_date = models.DateField(auto_now_add = True)

    # trainer_name = models.CharField(max_length = 50,choices = TrainerView.choices) # John Doe,James,Peter,Alex

    trainer = models.ForeignKey('trainers.Trainers',null=True,on_delete = models.SET_NULL)

    def __str__(self) :

        return f'{self.first_name} {self.last_name} {self.batch}'
    
    class Meta :

         verbose_name = 'students'

         verbose_name_plural = 'students'

         ordering = ['id']





