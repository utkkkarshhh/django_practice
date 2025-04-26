__all__ = [
    "BaseModel",
    "Classes",
    "Students",
    "Parents",
    "Teachers",
    "Subjects",
    "StudentParentMapping",
    "StudentSubjectMapping",
    "TeacherSubjectClassMapping",
]

from service.models.base_model import BaseModel
from service.models.classes import Classes
from service.models.students import Students
from service.models.parents import Parents
from service.models.subjects import Subjects
from service.models.teachers import Teachers
from service.models.student_parent_mapping import StudentParentMapping
from service.models.student_subject_mapping import StudentSubjectMapping
from service.models.teacher_subject_class_mapping import TeacherSubjectClassMapping
