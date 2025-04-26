from django.db import models

from service.models import BaseModel, Classes


class Students(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    admission_number = models.CharField(max_length=20, null=False, blank=False, unique=True)
    admission_date = models.DateTimeField(null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    student_email = models.EmailField(max_length=255, null=True, blank=True)
    dob = models.DateField(null=False, blank=False)
    address = models.TextField(null=False, blank=False)
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        db_table = 'students'
