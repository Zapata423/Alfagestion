from django.forms import ModelForm, Form
from django import forms
from .models import User, Role 

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'role', 'position', 'grade', 'password']
    
class RoleForm(ModelForm):
    class Meta:
        model = Role
        fields = ['name', 'description']
        
class UserLoginForm(Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))