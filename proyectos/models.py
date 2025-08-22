from django.db import models

class Project(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    progress_percentage = models.DecimalField(max_digits=2, decimal_places=2)
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    state = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




# Create your models here.
