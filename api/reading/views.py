from rest_framework import viewsets
from rest_framework import filters
from rest_framework import permissions
from api.permissions.permissions import CustomDjangoModelPermissions
from .models import Reading
from .serializers import ReadingSerializer


class ReadingViewSet(viewsets.ModelViewSet):
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer    
    permission_classes = (CustomDjangoModelPermissions, )    
    filter_backends = [filters.SearchFilter]
    search_fields = ['description']

    def get_queryset(self):
        return Reading.objects.filter(device__id=1)


# https://github.com/rpkilby/django-rest-framework-guardian
