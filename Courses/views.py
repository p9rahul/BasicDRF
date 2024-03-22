'''
# **** Generics view ****

from rest_framework import generics
from .serializers import SubjectSerializer, TeacherSerializer
from core.models import Teacher,Subject

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

'''

'''
# **** Viewset ****

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import SubjectSerializer, TeacherSerializer
from core.models import Teacher,Subject

class TeacherViewSet(ViewSet):

    def list(self, request):
        teachersQS = Teacher.objects.all()
        serialzer = TeacherSerializer(teachersQS, many=True)
        return Response(serialzer.data)
    
    def retrieve(self, request, pk):
        try:
            teacherQS= Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serialzer = TeacherSerializer(teacherQS)
        return Response(serialzer.data)
    
    def create(self, request):
        # teachersQS = Teacher.objects.all() not required
        serialzer = TeacherSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data)
        return Response(serialzer._errors)
'''

# **** ModelViewSet ****
from rest_framework.viewsets import ModelViewSet
from .serializers import SubjectSerializer, TeacherSerializer
from core.models import Teacher,Subject

class TeacherViewSet(ModelViewSet):

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class SubjectViewSet(ModelViewSet):

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer