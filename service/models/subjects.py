from django.db import models

from service.models import BaseModel


class Subjects(BaseModel):
    subject_types = (
        ('theory', 'Theory'),
        ('practical', 'Practical'),
        ('both', 'Both'),
    )

    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    subject_type = models.CharField(choices=subject_types, max_length=20, null=True, blank=True)
    credits = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'subject_master'
