from rest_framework import routers
from .views import EmployeeViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls))
]
