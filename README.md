# BasicDRF
Django Rest framework Basics

1) In this project - 
Courses app- Nested serializers concept implemented 
like - 1 Teacher has many subject

************************************
# Json Schema:
{
        "id": 3,
        "name": "john",
        "email": "john@test.com",
        "Subjects": [
            {
                "id": 2,
                "title": "cpp",
                "rating": 3,
                "teacher": 3
            }
        ]
    }
************************************
# Model:

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    #this method returns a human-readable string representation of an object in DB 
    def __str__(self):
        return self.email
    
class Subject(models.Model):
    title = models.CharField(max_length=20)
    rating = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='Subjects')
************************************
# Serializers:- ModelSerializer


from core.models import Teacher, Subject
from rest_framework import serializers

#ModelSerializer
class SubjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Subject
        fields ='__all__'

class TeacherSerializer(serializers.ModelSerializer):

    Subjects = SubjectSerializer(many=True, read_only=True)

    class Meta:
        model= Teacher
        fields =['id','name','email','Subjects']
        # fields ='__all__' #Order will not maintain doesn't look good

        read_only_fields = ('id',)

************************************
# Views used - Generics Views 
- package name -generics
- classes : 9 
- # Note - generics ->Very less code required as compare to mixin class, 
ListCreateAPIView - Concrete view for listing a queryset or creating a model instance.
https://www.django-rest-framework.org/api-guide/generic-views/

from rest_framework import generics
from .serializers import SubjectSerializer, TeacherSerializer
from core.models import Teacher,Subject

class TeacherListview(generics.ListCreateAPIView):
    
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

class SubjectListview(generics.ListCreateAPIView):

    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
************************************
# Urls.py - Project app level
from django.contrib import admin
from django.urls import path
from Courses.views import TeacherListview, SubjectListview

urlpatterns = [
    path('teachers', TeacherListview.as_view()),
    path('subjects', SubjectListview.as_view())

]

# Urls.py outer app level
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Courses.urls'))
]
************************************
# SQL - 
select * from [dbo].[core_subject]

select * from [dbo].[core_teacher]

select * from [dbo].[core_subject] sub
JOIN [dbo].[core_teacher] tec
on sub.teacher_id = tec.id
where tec.name='john'
=======================