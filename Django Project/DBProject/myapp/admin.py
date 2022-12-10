from django.contrib import admin
from .models import studinfo

# Register your models here.

class studAdmin(admin.ModelAdmin):
    list_display=['name','email','dob','address']

admin.site.register(studinfo,studAdmin)