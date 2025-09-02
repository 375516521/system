from django.db import models
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    admission_no = models.CharField(max_length=50, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    grade = models.CharField(max_length=20, blank=True)
    parent_contact = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to='students/photos/', null=True, blank=True)
    report_pdf = models.FileField(upload_to='students/reports/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def full_name(self): return f"{self.first_name} {self.last_name}"
    def __str__(self): return f"{self.admission_no} - {self.full_name()}"
