# from django.forms import ModelForm, Form
# from django import forms
# from .models import Usuario, Rol 

# class UserForm(ModelForm):
#     class Meta:
#         model = Usuario
#         fields = ['usuario', 'correo', 'nombre', 'apellido', 'rol', 'position', 'grade', 'password']
    
# class RoleForm(ModelForm):
#     class Meta:
#         model = Role
#         fields = ['name', 'description']
        
# class UserLoginForm(Form):
#     username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))