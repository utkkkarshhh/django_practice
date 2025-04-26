from django.db import models

from service.models import BaseModel


class Classes(BaseModel):
    name = models.IntegerField(null=False)
    is_board = models.BooleanField(null=False)

    class Meta:
        db_table = 'class_master'
