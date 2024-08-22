from django.contrib.auth.models import User
from django.db import models

# Department model
class Department(models.Model):
    name = models.CharField(max_length=100)
    diagnostics = models.TextField()
    location = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
#patient model

class PatientRecords(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_records')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_records')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    diagnostics = models.TextField()
    observations = models.TextField()
    treatments = models.TextField()
    misc = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Record {self.id} for {self.patient.username}'