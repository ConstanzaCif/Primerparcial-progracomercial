from django.shortcuts import render
from .models import Employee
from .serializer import EmployeeSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def destroy(self, request, *args, **kwargs):
        employee = self.get_object()
        employee.state = False
        employee.save()
        return Response({'detalle':'Empleado desactivado'}, status=status.HTTP_200_OK)

# Create your views here.
