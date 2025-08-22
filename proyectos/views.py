from django.shortcuts import render

from .models import Project, Assigments
from .serializer import ProjectSerializer, AssignSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    
    def destroy(self, request, *args, **kwargs):
        project = self.get_object()
        project.state = False
        project.save()
        return Response({'detalle':'Proyecto desactivado'}, status=status.HTTP_200_OK)

class AssigmentsViewset(viewsets.ModelViewSet):
    queryset = Assigments.objects.all()
    serializer_class = AssignSerializer
    
    def destroy(self, request, *args, **kwargs):
        assigment = self.get_object()
        assigment.state = False
        assigment.save()
        employee = assigment.employee()
        employee.project_assigned = False
        employee.save()
        return Response({'detalle':'Asignacion desactivado'}, status=status.HTTP_200_OK)

# Create your views here.