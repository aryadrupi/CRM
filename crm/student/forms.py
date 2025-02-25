from django import forms

from .models import Student,DistrictView,CourseChoices,BatchView,TrainerView

from batches.models import Batches

from courses.models import Courses

from trainers.models import Trainers

class StudentRegisterForm(forms.ModelForm) :

    class Meta :

        model = Student

        # fields = ['first_name','second_name','photo','email','contact_num',
        #          'house_name','post_office','district','pincode',
        #          'course','batch','batch_date','trainer_name']

        # fields = '__all__'

        exclude = ['adm_number','join_date','uuid','active_status','profile']

        widgets = {
                    'first_name':forms.TextInput(attrs = {'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                          'required':'required',
                                                         }),

                     'last_name':forms.TextInput(attrs = {'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                          'required':'required',
                                                         }),

                     'photo':forms.FileInput(attrs = {'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                     }),

                     'email':forms.TextInput(attrs = {'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                    'required':'required',
                                                    }),

                     'contact_num':forms.TextInput(attrs = {'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                          'required':'required',
                                                         }),

                     'house_name':forms.TextInput(attrs = {'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                          'required':'required',
                                                         }),

                     'post_office':forms.TextInput(attrs = {'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                          'required':'required',
                                                         }),

                     'pincode':forms.TextInput(attrs = {'class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                          'required':'required',
                                                         }),

                    #  'batch_date':forms.DateInput(attrs = {'type':'date','class':'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                    #                                       'required':'required',
                    #                                      }),
                                                       
                   }                                    

    district = forms.ChoiceField(choices = DistrictView.choices,widget = forms.Select(attrs = {
                                                                                                'class':'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
                                                                                                'required' :'required'
                                                                                            }))               
    
    # course = forms.ChoiceField(choices = CourseChoices.choices,widget = forms.Select(attrs = {
    #                                                                                             'class':'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
    #                                                                                             'required' :'required'
    #                                                                                         }))               
    course = forms.ModelChoiceField(queryset = Courses.objects.all(),widget = forms.Select(attrs = {'class':'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
                                                                                                'required' :'required'}))  
    # batch = forms.ChoiceField(choices = BatchView.choices,widget = forms.Select(attrs = {
    #                                                                                             'class':'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
    #                                                                                             'required' :'required'
    #                                                                                         }))               
    
    batch = forms.ModelChoiceField(queryset = Batches.objects.all(),widget = forms.Select(attrs = {'class':'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
                                                                                                'required' :'required'}))
    # trainer_name = forms.ChoiceField(choices = TrainerView.choices,widget = forms.Select(attrs = {
    #                                                                                             'class':'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
    #                                                                                             'required' :'required'
    #                                                                                         }))    

    trainer = forms.ModelChoiceField(queryset = Trainers.objects.all(),widget = forms.Select(attrs = {'class':'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
                                                                                                'required' :'required'}))

    
    def clean(self):

        cleaned_data = super().clean()

        pincode = cleaned_data.get('pincode')

        email =cleaned_data.get('email')

        if Student.objects.filter(profile__username=email).exists():
            
            self.add_error('email','this email is already registered.please change email')

        if len(pincode)<6 :

            self.add_error('pincode','pincode must be 6 digits')

        return cleaned_data
    
    def __init__(self,*args,**kwargs) :

        super(StudentRegisterForm,self).__init__(*args,**kwargs)

        if not self.instance :
            
            self.fields.get('photo').widget.attrs['required'] = 'required'