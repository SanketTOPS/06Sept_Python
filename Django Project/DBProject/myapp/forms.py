from django import forms
from .models import studinfo


class StudinfoForm(forms.ModelForm):
    class Meta:
        model=studinfo
        fields='__all__'
