from django.contrib import admin
from .models import Student
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('admission_no','first_name','last_name','grade','parent_contact','created_at')
    search_fields = ('admission_no','first_name','last_name')
    list_filter = ('grade',)
