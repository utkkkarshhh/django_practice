from django.db import models

from service.models import BaseModel, Classes, Subjects, Teachers


class TeacherSubjectClassMapping(BaseModel):
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE, null=False)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE, null=False)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'teacher_subject_class_mapping'
        constraints = [
            models.UniqueConstraint(fields=['teacher', 'subject', 'classes'], name='unique_teacher_subject_class')
        ]
