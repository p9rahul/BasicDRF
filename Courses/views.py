from rest_framework import generics
from .serializers import SubjectSerializer, TeacherSerializer
from core.models import Teacher,Subject

"""
Note - generics ->Very less code required as compare to mixin class,
- Here we need to create two methods oterwise if we keep in same class 2 arguments, issue will
"""
class TeacherListview(generics.ListCreateAPIView):
    
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

"""get with pk, update, destroy"""
class TeacherDetailsview(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

class SubjectListview(generics.ListCreateAPIView):

    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()

"""get with pk, update, destroy"""
class SubjectDetailsview(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
