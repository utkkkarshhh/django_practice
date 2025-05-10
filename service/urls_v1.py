from django.urls import path

from service.views import *

urlpatterns = [
    path('healthcheck', HealthCheckView.as_view(), name='health_check'),
    path('students/<int:id>/details', StudentDetailsView.as_view(), name='student_details'),
    path('teachers/<int:id>/details', TeacherDetailsView.as_view(), name='teacher_details'),
    path('class/<int:id>/details', ClassDetailsView.as_view(), name='class_details'),
]