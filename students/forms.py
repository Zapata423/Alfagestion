from django.forms import ModelForm
from django import forms
from .models import Student
from accounts.models import User


class StudentForm(ModelForm):
    
    class Meta:
        model = Student
        fields = ['telefono', 'fecha_nacimiento']
        widgets = {
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de teléfono'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'telefono': 'Teléfono',
            'fecha_nacimiento': 'Fecha de nacimiento',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # Si estamos editando un estudiante existente, cargar los datos del User
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['email'].initial = self.instance.user.email
            self.fields['grade'].initial = self.instance.user.grade
    
    def save(self, commit=True):
        student = super().save(commit=False)
        if commit:
            # Actualizar los datos del User asociado
            if student.user:
                student.user.first_name = self.cleaned_data['first_name']
                student.user.last_name = self.cleaned_data['last_name']
                student.user.email = self.cleaned_data['email']
                student.user.grade = self.cleaned_data['grade']
                student.user.save()
            student.save()
        return student
