from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from .models import Device


class DeviceAdmin(GuardedModelAdmin):
    pass


admin.site.register(Device, DeviceAdmin)
