from django.db import models

from service.models import BaseModel, Parents, Students


class StudentParentMapping(BaseModel):
    relationship_types = (
        ('mother', 'Mother'),
        ('father', 'Father'),
        ('guardian', 'Guardian')
    )
    
    student = models.ForeignKey(Students, on_delete=models.CASCADE, null=False)
    parent = models.ForeignKey(Parents, on_delete=models.CASCADE, null=False)
    relationship = models.CharField(
        max_length=20,
        choices=relationship_types,
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'student_parent_mapping'
        constraints = [
            models.UniqueConstraint(
                fields=['student_id', 'parent_id'],
                name='unique_student_parent_mapping'
            )
        ]
        indexes = [
            models.Index(fields=['student_id']),
            models.Index(fields=['parent_id']),
        ]

