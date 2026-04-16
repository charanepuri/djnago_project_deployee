from django.contrib import admin

# Register your models here.

from app.models import employee

class employee_admin(admin.ModelAdmin):
    list_display = ["name","email","phone","department"]
    
admin.site.register(employee,employee_admin)
