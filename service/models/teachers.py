from django.db import models

from service.models import BaseModel, Subjects


class Teachers(BaseModel):
    qualification_options = (
        ('Bachelors', 'Bachelors'),
        ('Masters', 'Masters'),
        ('PhD', 'PhD'),
    )
    
    role_options = (
        ('tgt', 'TGT'),
        ('pgt', 'PGT'),
        ('prt', 'PRT'),
        ('ntt', 'NTT'),
        ('other', 'Other'),
    )
    
    name = models.CharField(max_length=100, null=False, blank=False)
    dob = models.DateField(null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=False, blank=False)
    teacher_email = models.EmailField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    joining_date = models.DateField(null=False, blank=False)
    qualifications = models.CharField(choices=qualification_options, max_length=20, null=False, blank=False)
    role = models.CharField(choices=role_options, max_length=20, null=False, blank=False)
    primary_specialization = models.ForeignKey(Subjects, on_delete=models.CASCADE, null=False)
    
    class Meta:
        db_table = 'teachers'
