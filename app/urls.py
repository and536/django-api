from email.mime import base
from django.urls import include, path
from rest_framework import routers

from . import  exames, pacientes

router = routers.DefaultRouter()
router.register(r'pacientes', pacientes.PacienteViewSet, basename="pacientes")
router.register(r'exames', exames.ExameViewSet, basename="exames")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework'))
]