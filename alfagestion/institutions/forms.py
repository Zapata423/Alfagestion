from django.forms import ModelForm, Form
from django import forms
from .models import Activity, Institution, InstitutionManager

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['name', 'description', 'hours', 'date']

class InstitutionManagerForm(ModelForm):
    class Meta:
        model = InstitutionManager
        fields = ['name', 'last_name', 'phone', 'role_in_institution', 'observations',]

class InstitutionForm(ModelForm):
    class Meta:
        model = Institution
        fields = ['name', 'poblation_intervened', 'neighborhood', 'city', 'address', 'phone', 'contact_name', 'contact_email']

