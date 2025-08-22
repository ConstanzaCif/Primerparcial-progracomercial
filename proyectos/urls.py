from rest_framework import routers
from .views import ProjectViewSet, AssigmentsViewset
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'assigments', AssigmentsViewset)

urlpatterns = [
    path('', include(router.urls))
]
