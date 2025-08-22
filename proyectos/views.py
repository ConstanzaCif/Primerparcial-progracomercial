from django.shortcuts import render

from .models import Project, Assigments
from .serializer import ProjectSerializer, AssignSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from django.db import transaction

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    

    
    

class AssigmentsViewset(viewsets.ModelViewSet):
    queryset = Assigments.objects.all()
    serializer_class = AssignSerializer
    
    @transaction.atomic
    def destroy(self, request, *args, **kwargs):
            assignment = self.get_object()
            was_active = assignment.state
            emp = assignment.employee           

            assignment.state = False
            assignment.save(update_fields=['state'])

            if was_active:
                still_active = Assigments.objects.filter(
                    employee=emp, state=True
                ).exclude(pk=assignment.pk).exists()

                if not still_active and bool(emp.project_assigned):
                    emp.project_assigned = False
                    emp.save(update_fields=['project_assigned'])

            return Response({'detail': 'Asignación desactivada'}, status=status.HTTP_200_OK)

# Create your views here.