import random
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand
from faker import Faker

from service.models import (Classes, Parents, StudentParentMapping, Students,
                            StudentSubjectMapping, Subjects, Teachers,
                            TeacherSubjectClassMapping)


class Command(BaseCommand):
    help = "Populate school database with sample data"

    def handle(self, *args, **kwargs):
        fake = Faker()

        self.stdout.write(self.style.WARNING("Deleting old data..."))
        StudentParentMapping.objects.all().delete()
        StudentSubjectMapping.objects.all().delete()
        TeacherSubjectClassMapping.objects.all().delete()
        Students.objects.all().delete()
        Teachers.objects.all().delete()
        Parents.objects.all().delete()
        Classes.objects.all().delete()
        Subjects.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("Old data cleared."))

        # ---------- CLASSES ----------
        self.stdout.write("Creating Classes...")
        classes = [Classes(name=i, is_board=bool(i % 2)) for i in range(1, 13)]
        Classes.objects.bulk_create(classes)
        classes = list(Classes.objects.all())

        # ---------- SUBJECTS ----------
        self.stdout.write("Creating Subjects...")
        subject_types = ['theory', 'practical', 'both']
        subjects = [
            Subjects(
                name=f"Subject {i}",
                code=f"SUBJ{i:03}",
                description=fake.text(max_nb_chars=50),
                subject_type=random.choice(subject_types),
                credits=random.randint(2, 5)
            )
            for i in range(1, 21)
        ]
        Subjects.objects.bulk_create(subjects)
        subjects = list(Subjects.objects.all())

        # ---------- PARENTS ----------
        self.stdout.write("Creating Parents...")
        parents = [
            Parents(
                name=fake.name(),
                phone_number=fake.phone_number(),
                email=fake.email(),
                address=fake.address(),
                dob=fake.date_of_birth(minimum_age=30, maximum_age=60),
                occupation=fake.job()
            )
            for _ in range(200)
        ]
        Parents.objects.bulk_create(parents)
        parents = list(Parents.objects.all())

        # ---------- STUDENTS ----------
        self.stdout.write("Creating Students...")
        students = []
        for i in range(500):
            students.append(
                Students(
                    name=fake.name(),
                    admission_number=f"ADM{i:04}",
                    admission_date=fake.date_time_between(start_date="-3y", end_date="now"),
                    phone_number=fake.phone_number(),
                    student_email=fake.email(),
                    dob=fake.date_of_birth(minimum_age=6, maximum_age=18),
                    address=fake.address(),
                    classes=random.choice(classes),
                )
            )
        Students.objects.bulk_create(students)
        students = list(Students.objects.all())

        # ---------- TEACHERS ----------
        self.stdout.write("Creating Teachers...")
        qualifications = ['Bachelors', 'Masters', 'PhD']
        roles = ['tgt', 'pgt', 'prt', 'ntt', 'other']
        teachers = []
        for _ in range(100):
            teachers.append(
                Teachers(
                    name=fake.name(),
                    dob=fake.date_of_birth(minimum_age=25, maximum_age=60),
                    phone_number=fake.phone_number()[:15],
                    teacher_email=fake.email(),
                    address=fake.address(),
                    joining_date=fake.date_between(start_date="-10y", end_date="today"),
                    qualifications=random.choice(qualifications),
                    role=random.choice(roles),
                    primary_specialization=random.choice(subjects),
                )
            )
        Teachers.objects.bulk_create(teachers)
        teachers = list(Teachers.objects.all())

        # ---------- STUDENT-PARENT MAPPING ----------
        self.stdout.write("Mapping Students to Parents...")
        relationship_types = ['mother', 'father', 'guardian']
        mappings = []
        for student in students:
            for _ in range(random.randint(1, 2)):  # 1–2 parents
                parent = random.choice(parents)
                mappings.append(
                    StudentParentMapping(
                        student=student,
                        parent=parent,
                        relationship=random.choice(relationship_types)
                    )
                )
        StudentParentMapping.objects.bulk_create(mappings, ignore_conflicts=True)

        # ---------- STUDENT-SUBJECT MAPPING ----------
        self.stdout.write("Mapping Students to Subjects...")
        mappings = []
        for student in students:
            chosen_subjects = random.sample(subjects, random.randint(3, 6))
            for subj in chosen_subjects:
                mappings.append(StudentSubjectMapping(student=student, subject=subj))
        StudentSubjectMapping.objects.bulk_create(mappings, ignore_conflicts=True)

        # ---------- TEACHER-SUBJECT-CLASS MAPPING ----------
        self.stdout.write("Mapping Teachers to Subjects and Classes...")
        mappings = []
        for teacher in teachers:
            chosen_subjects = random.sample(subjects, random.randint(1, 3))
            chosen_classes = random.sample(classes, random.randint(1, 3))
            for subj in chosen_subjects:
                for cls in chosen_classes:
                    mappings.append(
                        TeacherSubjectClassMapping(teacher=teacher, subject=subj, classes=cls)
                    )
        TeacherSubjectClassMapping.objects.bulk_create(mappings, ignore_conflicts=True)

        self.stdout.write(self.style.SUCCESS("Database populated successfully! 🚀"))
