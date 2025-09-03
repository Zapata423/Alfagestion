from django.db import models
from django.utils import timezone
from accounts.models import User


class Teacher(models.Model):
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE, related_name='teacher_profile', verbose_name="Usuario", null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Teléfono")
    
    class Meta:
        verbose_name = "Docente"
        verbose_name_plural = "Docentes"
        ordering = ['user__last_name', 'user__first_name']
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.user.position}"
    
    @property
    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    @property
    def first_name(self):
        return self.user.first_name
    
    @property
    def last_name(self):
        return self.user.last_name
    
    @property
    def email(self):
        return self.user.email
    
    @property
    def position(self):
        return self.user.position
    
    @property
    def date_joined(self):
        return self.user.date_joined

