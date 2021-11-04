from django.contrib import admin
from .models import Exhibitor
# Register your models here.

class ExhibitorAdmin(admin.ModelAdmin):
    # model = Exhibitor
    list_display = ['email','name','brand_name']
    search_fields = ['email','name','brand_name']

admin.site.register(Exhibitor,ExhibitorAdmin)
