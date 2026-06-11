from tkinter.constants import CASCADE

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Jobapplication(models.Model):
    STATUS_CHOICES=[
        ('Applied','Applied'),
        ('Interview','Interview'),
        ('Rejected','Rejected'),
        ('Hired','Hired'),
    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    company_name=models.CharField(max_length=100)
    job_title=models.CharField(max_length=200)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='Applied')
    date_applied=models.DateField(auto_now_add=True)
    notes=models.TextField(blank=True)

    def __str__(self):
        return  f"{self.company_name}---{self.job_title}"
