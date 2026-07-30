from django import forms
from .models import Employee
from django.contrib.auth.models import User

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = "__all__"


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
        ]