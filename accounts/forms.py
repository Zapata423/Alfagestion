from django import forms
from .models import Usuario
from django.contrib.auth import authenticate

class UserRegisterForm(forms.ModelForm):

  password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
              attrs={
                  'placeholder': 'Contraseña',
                  'style': '{ margin 10px}'
              }
        )
    )
  password2 = forms.CharField(
      label='Contraseña',
      required=True,
      widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir Contraseña',
                'style': '{ margin 10px}'
            }
      )
    )
  class Meta:
        model = Usuario
        fields = (
          'email' ,
          'rol',
          'estudiante',
          'docente',
          'cargo',
          'grado',
          )
  def clean_password2(self):
      if self.cleaned_data['password1'] != self.cleaned_data['password2']:
          self.add_error('password2', 'Las contraseñas no son las mismas')


class LoginForm(forms.Form):
    
    email = forms.CharField(
      label='email',
      required=True,
      widget=forms.TextInput(
            attrs={
                'placeholder': 'email',
                'style': '{ margin 10px}'
            }
      )
  )
    
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
              attrs={
                  'placeholder': 'Contraseña',
                  'style': '{ margin 10px}'
              }
        )
    )
    
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = self.cleaned_data['email'] 
        password = self.cleaned_data['password'] 
        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Los datos del Usuario no son correctos')
        
        return self.cleaned_data