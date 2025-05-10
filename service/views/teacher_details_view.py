from rest_framework.views import APIView

class TeacherDetailsView(APIView):
    
    def get(self, request, id: int):
        pass