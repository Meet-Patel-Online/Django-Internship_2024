from django.forms import ModelForm
from .models import student

class StudentForm(ModelForm):
    class Meta:
        model = student
        field = ["sname","semail","spassword"]
        exclude = ['createdAD']