from django.contrib import admin
from .models import Student, Department
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=["name","age","email"]

class DepartmentAdmin(admin.ModelAdmin):
    list_display=["name","faculty","numberofstudents"]

admin.site.register(Student, StudentAdmin)
admin.site.register(Department, DepartmentAdmin)