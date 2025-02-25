from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class RoleChoice(models.TextChoices) :

    ADMIN = 'Admin','Admin'

    STUDENT = 'Student','Student'

    ACADEMIC_COUNSELLOR = 'Academic_counsellor','Academic_counsellor'

    TRAINER = 'Trainer','Trainer'

    SALES = 'Sales','Sales'

class Profile(AbstractUser) :

    role = models.CharField(max_length=30,choices=RoleChoice.choices)

    def __str__(self):

        return f'{self.username}-{self.role}'
    
    class Meta :

        verbose_name = 'profile'

        verbose_name_plural = 'profile'

