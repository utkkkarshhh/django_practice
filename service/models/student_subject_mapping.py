from django.db import models

from service.models import BaseModel, Students, Subjects


class StudentSubjectMapping(BaseModel):
    student = models.ForeignKey(Students, on_delete=models.CASCADE, null=False)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'student_subject_mapping'
