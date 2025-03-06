import uuid

from . models import Trainers

import string

import random

def get_employee_number() :

    while True :

        pattern = str(uuid.uuid4().int)[:2]

        employee = f'LM-E{pattern}'

        if not Trainers.objects.filter(employee_id = employee).exists() :

            return employee
        
def get_password() :

    password =''.join(random.choices(string.ascii_letters+string.digits,k=8))

    return password

    





