from django.db import models
from django.utils import timezone
from institutions.models import Institution

# actividades, evidencia, calendario

class Activity(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.SET_NULL, null=True, related_name="activities")
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    hours = models.PositiveIntegerField()
    date = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)  # default current date & time

    def __str__(self):
        return f"{self.name} ({self.institution})"
