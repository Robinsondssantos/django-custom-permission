from rest_framework import viewsets
from rest_framework_guardian import filters
from api.permissions.permissions import CustomDjangoObjectPermissions
from .models import Device
from .serializers import DeviceSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = (CustomDjangoObjectPermissions, )
    filter_backends = [filters.ObjectPermissionsFilter]
    search_fields = ['description']