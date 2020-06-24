from django.contrib import admin
from .models import Wpis, Category

@admin.register(Wpis)
class WpisAdmin(admin.ModelAdmin):
    list_display = ( 'id','name','cat','note')

admin.site.register(Category)