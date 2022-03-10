from django import forms
from .models import User

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['last_login','is_admin','is_active']