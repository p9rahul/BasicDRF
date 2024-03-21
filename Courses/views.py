from rest_framework import generics
from .serializers import SubjectSerializer, TeacherSerializer
from core.models import Teacher,Subject

# Note - generics ->Very less code required as compare to mixin class, 
class TeacherListview(generics.ListCreateAPIView):
    
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

class SubjectListview(generics.ListCreateAPIView):

    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
