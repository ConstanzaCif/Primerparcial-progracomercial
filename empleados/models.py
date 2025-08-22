from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dpi = models.CharField(max_length=13)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    hire_date = models.DateField()
    project_assigned = models.BooleanField(default= False, null=True, blank=True)
    state = models.BooleanField(default= True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name




# Create your models here.
