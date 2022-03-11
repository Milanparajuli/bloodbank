from django import forms
from .models import User
from blood.models import BloodGroup

class UserCreationForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs = {'class':'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_of_birth = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','type':'date'}))
    citizenShipNo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    bloodGroup = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),queryset= BloodGroup.objects.all())
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        exclude = ['last_login','is_admin','is_active']