__all__ = [
    "StudentDetailsView",
    "ClassDetailsView",
    "TeacherDetailsView",
    "HealthCheckView",
]

from service.views.healthcheck import HealthCheckView
from service.views.student_details_view import StudentDetailsView
from service.views.class_details_view import ClassDetailsView
from service.views.teacher_details_view import TeacherDetailsView
