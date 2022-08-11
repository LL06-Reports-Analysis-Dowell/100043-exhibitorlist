# from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Event
# Register your models here.

# class EventResource(resources.ModelResource):
#     class Meta:
#         model=Event
#         use_bulk=True
#         batch_size = 1000
#         force_init_instance = True

class EventAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # resource_class=EventResource
    pass
admin.site.register(Event,EventAdmin)
