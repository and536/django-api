from rest_framework import viewsets
from datetime import datetime
from rest_framework import permissions
from app.models import Exame
from app.serializers import ExameSerializer
from rest_framework import status
from rest_framework.response import Response


class ExameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Exame.objects.all()
    serializer_class = ExameSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = (permissions.AllowAny,) 

    def list(self, request):
        queryset = Exame.objects.all()
        serializer = self.serializer_class(self.queryset, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        instance = self.get_object()
        # query = request.GET.get('query', None)  # read extra data
        return Response(self.serializer_class(instance).data,
                        status=status.HTTP_200_OK)
                    
    def create(self, request):
        data = {
            "name_professional": request.POST.get('name_professional', None),
            "date_exam": request.POST.get('date_exam', None),
            "weight": request.POST.get('weight', None),
            "height": request.POST.get('height', None),
            "patient": request.POST.get('patient', None),
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
            "name_professional": request.POST.get('name_professional', None),
            "date_exam": request.POST.get('date_exam', None),
            "weight": request.POST.get('weight', None),
            "height": request.POST.get('height', None),
            "patient": request.POST.get('patient', None),
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
        
        return super(ExameViewSet, self).destroy(request, pk)