from django import forms
from .models import usersignup,mynotes

class signupForm(forms.ModelForm):
    class Meta:
        model=usersignup
        fields='__all__'
    

class notesForm(forms.ModelForm):
    class Meta:
        model=mynotes
        fields='__all__'