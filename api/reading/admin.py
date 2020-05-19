from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from .models import Reading


class ReadingAdmin(GuardedModelAdmin):
    pass


admin.site.register(Reading, ReadingAdmin)
