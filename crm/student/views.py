from django.shortcuts import render,redirect,get_object_or_404

from .models import DistrictView,CourseChoices,TrainerView,BatchView

from . utility import get_admission_number,get_password,send_email

from django.views.generic import View

from .models import Student

from .forms import StudentRegisterForm

from django.db.models import Q

from django.db import transaction

from authentication.models import Profile

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from authentication.permissions import permission_roles

import threading

import datetime

# Create your views here.

class GetStudentObject :

    def get_student(self,request,uuid) :

        try :

             student = Student.objects.get(uuid=uuid)

             return student

        except :

             return render(request,'errorpages/error-404.html')
        
#@method_decorator(login_required(login_url='login'),name = 'dispatch')


class Dashboardview(View):

    def get(self,request,*args,**kwargs):

        return render(request,'student/dashboard.html')
    
# roles Sales,Admin,Trainer,Academin Counsillor
# @method_decorator(permission_roles(roles=['Admin','Sales','Trainer','Academin Counsiller']),name='dispatch')

class StudentListview(View):

    def get(self,request,*args,**kwargs):

        query = request.GET.get('query')

        role = request.user.role

        if role in ['Trainer'] :
             
             students = Student.objects.filter(active_status = True,trainer__profile = request.user)

             if query :

                    students= Student.objects.filter(Q(active_status=True)&Q(trainer__profile=request.user)&(Q(first_name__icontains=query)|
                                                                    Q(last_name__icontains=query)|
                                                                    Q(email__exact=query)|
                                                                    Q(contact_num__icontains=query)|
                                                                    Q(house_name__icontains=query)|
                                                                    Q(post_office__icontains=query)|
                                                                    Q(district__icontains=query)|
                                                                    Q(pincode__icontains=query)|
                                                                    Q(adm_number__icontains=query)|
                                                                    Q(course__code__icontains=query)|
                                                                    Q(batch__name__icontains=query)|
                                                                    Q(trainer__first_name__icontains=query)))
                    
        if role in ['Academic_counsellor'] :
             
             students = Student.objects.filter(active_status = True,batch__academic_counsellor__profile = request.user)

             if query :

                    students= Student.objects.filter(Q(active_status=True)&Q(batch__academic_counsellor__profile=request.user)&(Q(first_name__icontains=query)|
                                                                    Q(last_name__icontains=query)|
                                                                    Q(email__exact=query)|
                                                                    Q(contact_num__icontains=query)|
                                                                    Q(house_name__icontains=query)|
                                                                    Q(post_office__icontains=query)|
                                                                    Q(district__icontains=query)|
                                                                    Q(pincode__icontains=query)|
                                                                    Q(adm_number__icontains=query)|
                                                                    Q(course__code__icontains=query)|
                                                                    Q(batch__name__icontains=query)|
                                                                    Q(batch__academic_counsellor__first_name__icontains=query)))            
        else :

             students = Student.objects.filter(active_status = True)

             if query :

                students= Student.objects.filter(Q(active_status=True)&(Q(first_name__icontains=query)|
                                                                    Q(last_name__icontains=query)|
                                                                    Q(email__exact=query)|
                                                                    Q(contact_num__icontains=query)|
                                                                    Q(house_name__icontains=query)|
                                                                    Q(post_office__icontains=query)|
                                                                    Q(district__icontains=query)|
                                                                    Q(pincode__icontains=query)|
                                                                    Q(adm_number__icontains=query)|
                                                                    Q(course__code__icontains=query)|
                                                                    Q(batch__name__icontains=query)|
                                                                    Q(trainer__first_name__icontains=query)))


        data = {'students':students,'query':query}

        return render(request,'student/students.html',context=data)

# roles   Admin,Sales
# @method_decorator(permission_roles(roles=['Admin','Sales']),name='dispatch')

class FormView(View):

    def get(self,request,*args,**kwargs):

        form = StudentRegisterForm()

        # data = {'districts' :DistrictView,'courses' :CourseChoices,'batches' :BatchView,'trainees' :TrainerView,'form' :form}

        data = {'form':form,}
    
        return render(request,'student/form.html',context = data)
    
    def post(self,request,*args,**kwargs) :

        form = StudentRegisterForm(request.POST,request.FILES)

        if form.is_valid() :

            with transaction.atomic() :

                Student = form.save(commit = False)

                Student.adm_number = get_admission_number()

                # Student.join_date = '2025-02-05'

                username = Student.email

                password = get_password()

                print(password)

                profile = Profile.objects.create_user(username = username,password = password,role = 'Student')

                Student.profile = profile

                Student.save()

                # sending login credentials to student through mail

                subject = 'Login Credential'

                recipients = [Student.email]

                template = 'email/login_credential.html'

                join_date = Student.join_date

                date_after_10_days = join_date + datetime.timedelta(days=10)

                print(date_after_10_days)

                context = {'name':f'{Student.first_name} {Student.last_name}','username':username,'password':password,'date_after_10_days':date_after_10_days}

                # send_email(subject,recipients,template,context)

                thread = threading.Thread(target=send_email,args=(subject,recipients,template,context))

                thread.start()

            return redirect('students')
        
        else :

             data = {'form':form}

             return render(request,'student/form.html',context = data)

        # form_data = request.POST

        # first_name = form_data.get('first_name')

        # last_name = form_data.get('last_name')

        # photo = request.FILES.get('photo')

        # email = form_data.get('email')

        # contact_number = form_data.get('contact_number')

        # house_name = form_data.get('house_name')

        # post_office = form_data.get('post_office')

        # district = form_data.get('district')

        # pincode = form_data.get('pincode')

        # course = form_data.get('course')

        # batch = form_data.get('batch')

        # batch_date = form_data.get('batch_date')

        # trainer = form_data.get('trainer')

        # admission_number = get_admission_number()

        # join_date = '2024-08-16'

        # Student.objects.create(first_name = first_name,
        #                        last_name = last_name,
        #                        photo = photo,email = email,
        #                        contact_num = contact_number,
        #                        house_name = house_name,
        #                        post_office = post_office,
        #                        district = district,
        #                        pincode = pincode,
        #                        adm_number = admission_number,
        #                        course = course,
        #                        batch = batch,
        #                        batch_date = batch_date,
        #                        join_date = join_date,
        #                        trainer_name = trainer)

        # print(first_name,last_name,photo,email,contact_number,house_name,post_office,district,pincode,course,batch,batch_date,trainer,admission_number,join_date)
@method_decorator(permission_roles(roles=['Admin','Sales','Trainer','Academin Counsiller']),name='dispatch')
class StudentDetailView(View) :

        def get(self,request,*args,**kwargs) :

            uuid = kwargs.get('uuid')

            # student = get_object_or_404(Student,pk=pk)

            student = GetStudentObject().get_student(request,uuid)

            # students = Student.objects.filter(active_status = True)

            # try :

            #     student = Student.objects.get(pk=pk)

            # except :

            #     return redirect('error-404')

            data = {'student':student}

            return render(request,'student/student-detail.html',context = data)
        
@method_decorator(permission_roles(roles=['Admin','Sales']),name='dispatch')  
class StudentDeleteView(View) :

    def get(self,request,*args,**kwargs) :

        uuid = kwargs.get('uuid')

        student = GetStudentObject().get_student(request,uuid)

        # try :

        #      student = Student.objects.get(pk=pk)

        # except :

        #         return redirect('error-404')
        
        # student.delete()

        student.active_status = False

        student.save()

        return redirect('students')
@method_decorator(permission_roles(roles=['Admin','Sales']),name='dispatch')

class StudentUpdateView(View) :
     
     def get(self,request,*args,**kwargs) :
          
          uuid = kwargs.get('uuid')

          student = GetStudentObject().get_student(request,uuid)

          form = StudentRegisterForm(instance = student)

          data = {'form':form}
          
          return render(request,'student/student-update.html',context = data)
     
     def post(self,request,*args,**kwargs) :
          
          uuid = kwargs.get('uuid')

          student = GetStudentObject().get_student(request,uuid)
          
          form = StudentRegisterForm(request.POST,request.FILES,instance = student)

          if form.is_valid() :
               
               form.save()

               return redirect('students')
          
          else :
               
               data = {'form':form}
               
               return render(request,'student/student-update.html',context = data)



