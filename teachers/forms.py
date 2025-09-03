from django.forms import ModelForm
from django import forms
from .models import Teacher
from accounts.models import User


class TeacherForm(ModelForm):
    # Campos del User que se mostrarán en el formulario
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el apellido'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@ejemplo.com'}))
    position = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Professor, Coordinator, Director'}))
    
    class Meta:
        model = Teacher
        fields = ['phone']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de teléfono'}),
        }
        labels = {
            'phone': 'Teléfono',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # Si estamos editando un docente existente, cargar los datos del User
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['email'].initial = self.instance.user.email
            self.fields['position'].initial = self.instance.user.position
    
    def save(self, commit=True):
        teacher = super().save(commit=False)
        if commit:
            # Actualizar los datos del User asociado
            if teacher.user:
                teacher.user.first_name = self.cleaned_data['first_name']
                teacher.user.last_name = self.cleaned_data['last_name']
                teacher.user.email = self.cleaned_data['email']
                teacher.user.position = self.cleaned_data['position']
                teacher.user.save()
            teacher.save()
        return teacher
