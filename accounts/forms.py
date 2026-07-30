from django import forms
from django.contrib.auth.models import User

class Registerform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
        ]

    def clean(self):
        self.cleaned_data  = super().clean()
        self.password = self.cleaned_data.get('password')
        self.confirm_password = self.cleaned_data.get('confirm_password')

        if self.password != self.confirm_password:
            raise forms.ValidationError("Password do not match")

        return self.cleaned_data