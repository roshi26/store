from django import forms
from attendence.models import Attendence


attendence_choices=(
     ('absent', 'Absent'),
     ('present', 'Present')
    )
class AttendenceForm(forms.Form):
  employee_name=forms.CharField()
  designation=forms.CharField()
  signin_time=forms.DateTimeField()
  signout_time=forms.DateTimeField()
  attendence_choices=forms.ChoiceField(choices=attendence_choices)
