from gettext import translation
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import inlineformset_factory, DateTimeField
from django.utils import timezone
from pip._internal.utils._jaraco_text import _

from worktime.models import Employer, Employee, Timesheet, CustomUser, WorkTime


class MyAuthForm(AuthenticationForm):
    # Сейчас из темплейта сообщения
    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("This account is inactive."),
    }

class EmployerForm(forms.ModelForm):

    class Meta:
        model = Employer
        fields = ['name', 'customuser']
        
class EmployerFormDoubleform(forms.ModelForm):

    class Meta:
        model = Employer
        fields = ['id', 'customuser']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class EmployerDoubleformWithourCustomuser(forms.ModelForm):# Форма для создания Employer с 2мя формами, во вьюхе ф.CustomuserCreateWithDoubleForm

    class Meta:
        model = Employer
        fields = ['name']

class EmployeeDoubleForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'employer']

class CustomUserDoubleform(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
        exclude = ['full_name']


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
        # exclude = ['full_name']


EmployeeFormSet = inlineformset_factory(CustomUser, Employee, form=CustomUserForm,
                                        formset=EmployeeForm,
                                        extra=1, max_num=20, can_delete=False)

    

class TimesheetForm(forms.ModelForm):
    datetime_start = DateTimeField(
        # widget=DatePickerInput(format='%y-%m-%d'), Если раскомментировать, вылезает предупреждение, что надо формат , видимо на темплейте тоже создать
                                   
                         input_formats=('%y-%m-%d',),
                         required=False,
                         )
                         
    datetime_complete = DateTimeField(
        #widget=DatePickerInput(format='%y-%m-%'),
                                      
                         input_formats=('%y-%m-%d',),
                         required=False,
                         )
    

    class Meta:
        model = Timesheet
        # fields = '__all__'
        fields = ['datetime_start', 'datetime_complete', 'status_work', 'employee']
        widgets = {
            "datetime_start": DatePickerInput(options={"format": "y-m-d", "value": timezone.now().strftime("%Y-%m-%d")}),
            "datetime_complete": DatePickerInput(options={"format": "y-m-d", "value": timezone.now().strftime("%Y-%m-%d")})
              }
        

class TimesheetCreationForm(forms.ModelForm):
  
    

    class Meta:
        model = Timesheet
        fields = '__all__'
        exclude = ['datetime_start', 'datetime_complete',]
        widgets = {
            "datetime_start": DatePickerInput(options={"format": "y-m-d H-M", "value": timezone.now().strftime("%Y-%m-%d %H-%M")}),
            "datetime_complete": DatePickerInput(options={"format": "y-m-d H-M", "value": timezone.now().strftime("%Y-%m-%d %H-%M")})
              }


class WorkTimeForm(forms.ModelForm):

    class Meta:
        model = WorkTime
        fields = '__all__'

