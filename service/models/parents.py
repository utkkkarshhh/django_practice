from django.db import models

from service.models import BaseModel


class Parents(BaseModel):
    name = models.CharField(max_length=255, blank=False, null=False)
    phone_number = models.CharField(max_length=15, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(max_length=255, null=True, blank=True)
    dob = models.DateField(null=False, blank=False)
    occupation = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'parents'
