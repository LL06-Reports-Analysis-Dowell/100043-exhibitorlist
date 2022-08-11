from django.contrib import admin
from .models import Details
# Register your models here.

from import_export.admin import ExportActionMixin

# Register your models here.
class BookAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('venue', 'city', 'country', 'BDEventID')

admin.site.register(Details, BookAdmin)
