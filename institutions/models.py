from django.db import models
from django.utils import timezone


class Institution(models.Model):
    name = models.CharField(max_length=200)
    poblation_intervened = models.CharField(max_length=100, blank=True, null=True)
    neighborhood = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    contact_name = models.CharField(max_length=150, blank=True, null=True)
    contact_email = models.EmailField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class InstitutionManager(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, blank=True, null=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name="managers")
    role_in_institution = models.CharField(max_length=100, blank=True, null=True)
    observation = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.institution}"


