from rest_framework.views import APIView

from service.models import Students, StudentParentMapping, StudentSubjectMapping

class StudentDetailsView(APIView):
    
    def get(self, request, id: int):
        pass
    
    
    response = {
        'success': True,
        'data': {
            'student': {
                'id': 1,
                'name': 'John Doe',
                'admission_number': 'AD12345',
                'admission_date': '2023-01-01',
                'phone_number': '1234567890',
                'student_email': '',
                'dob': '2005-01-01',
                'address': '123 Main St, City, Country',
                'classes': {
                    'id': 1,
                    'name': '10',
                }
                    
            },
            'parents': [
                {
                    'id': 1,
                    'name': 'Jane Doe',
                    'phone_number': '0987654321',
                    'address': '123 Main St, City, Country',
                    'email': '',
                    'dob': '1980-01-01',
                    'occupation': 'Engineer',
                    'relationship': 'Mother'
                },
                {
                    'id': 2,
                    'name': 'John Smith',
                    'phone_number': '1122334455',
                    'address': '456 Elm St, City, Country',
                    'email': '',
                    'dob': '1985-01-01',
                    'occupation': 'Doctor',
                    'relationship': 'Father'
                }
            ],
            'subjects': [
                {
                    'id': 1,
                    'name': 'Mathematics',
                    'code': 'MATH101',
                    'description': 'Basic Mathematics',
                    'subject_type': 'theory',
                    'credits': 3,
                    'teacher': {
                        'id': 1,
                        'name': 'Mr. Smith'
                    }
                },
                {
                    'id': 2,
                    'name': 'Science',
                    'code': 'SCI101',
                    'description': 'Basic Science',
                    'subject_type': 'both',
                    'credits': 4,
                    'teacher': {
                        'id': 2,
                        'name': 'Ms. Johnson'
                    }
                }
            ]
        }
    }