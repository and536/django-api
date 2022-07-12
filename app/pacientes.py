from datetime import datetime
from rest_framework import viewsets
from rest_framework import permissions
from app.models import Paciente
from app.serializers import PacienteSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

class PacienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = (permissions.AllowAny,) 

    def list(self, request):
        queryset = Paciente.objects.all()
        serializer = self.serializer_class(self.queryset, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        instance = self.get_object()
        # query = request.GET.get('query', None)  # read extra data
        return Response(self.serializer_class(instance).data,
                        status=status.HTTP_200_OK)
                    
    def create(self, request):
        data = {
            "name" : request.POST.get('name', None),
            "age" : request.POST.get('age', None),
            "address" : request.POST.get('address', None),
            "created_at": datetime.now()
        }
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        instance = self.get_object()
        data = {
            "name" : request.POST.get('name', None),
            "age" : request.POST.get('age', None),
            "address" : request.POST.get('address', None),
            "created_at": datetime.now()
        }
        serializer = self.serializer_class(instance=instance,
                                            data=data,
                                            partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        instance = self.get_object()
        
        return super(PacienteViewSet, self).destroy(request, pk)