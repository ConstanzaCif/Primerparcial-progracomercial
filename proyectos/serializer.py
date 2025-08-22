from rest_framework import serializers

from .models import Project, Assigments
from empleados.models import Employee
from empleados.serializer import EmployeeSerializer
from django.db import transaction

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class AssignSerializer(serializers.ModelSerializer):
    # employee = EmployeeSerializer(read_only = True)
    # project = ProjectSerializer(read_only = True)
    class Meta:
        model = Assigments
        fields = '__all__'
    
    def validate(self, attrs):
        employee = attrs["employee"]
        will_be_active = attrs.get('project_assigned', True)
        if will_be_active and employee.project_assigned:
            raise serializers.ValidationError(
                {'employee': 'El empleado ya tiene una asignación activa.'}
            )
        return attrs
    
    @transaction.atomic
    def create(self, validated_data):
        assignment = super().create(validated_data)

        if assignment.state and not assignment.employee.project_assigned:
            assignment.employee.project_assigned = True
            assignment.employee.save(update_fields=['project_assigned'])

        return assignment

        