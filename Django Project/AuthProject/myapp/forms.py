from django import forms
from .models import usersignup


class usersignupForm(forms.ModelForm):
    class Meta:
        model=usersignup
        fields='__all__'