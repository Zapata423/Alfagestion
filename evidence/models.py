from django.db import models
from django.utils import timezone
from institutions.models import Institution
from students.models import Student
from model_utils.models import TimeStampedModel

# actividades, evidencia, calendario

class Activity(TimeStampedModel):
    institution = models.ForeignKey(Institution, on_delete=models.SET_NULL, null=True, related_name="activities")
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    hours = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.institution})"
    

class Evidence(TimeStampedModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="evidence")
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="evidence")
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to="evidence/")
    mime_type = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Evidencia de {self.student} en {self.activity}"

