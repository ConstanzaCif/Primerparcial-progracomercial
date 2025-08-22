from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Q

class Project(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    progress_percentage = models.DecimalField(
        max_digits=5, decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0
    )
    project_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    state = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name

class Assigments(models.Model):
    assignment_date = models.DateField(auto_now_add=True)
    employee = models.ForeignKey("empleados.Employee", on_delete=models.PROTECT, related_name="assignments")
    project = models.ForeignKey(Project, on_delete=models.PROTECT, related_name="assignments")
    state = models.BooleanField(default=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




# Create your models here.
