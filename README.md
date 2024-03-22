# BasicDRF
Django Rest framework Basics

1) In this project - 
Courses app- Nested serializers concept implemented 
- like 1 Teacher has many subject
- Generics views - Class - ListCreateAPIView (get and post not put,delete)
- Serializers:- ModelSerializer
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

#__str__ method returns a human-readable string representation of an object in DB 
#
class Teacher(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.email
        
#Subject model
#
class Subject(models.Model):

    title = models.CharField(max_length=20)
    rating = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='Subjects')

************************************
# Serializers:- ModelSerializer


from core.models import Teacher, Subject
from rest_framework import serializers

#
class SubjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Subject
        fields ='__all__'

#
class TeacherSerializer(serializers.ModelSerializer):

    Subjects = SubjectSerializer(many=True, read_only=True)

    class Meta:
        model= Teacher
        fields =['id','name','email','Subjects']
        # fields ='__all__' #Order will not maintain doesn't look good

        read_only_fields = ('id',)

************************************
# Generics Views
- package name -generics
- classes : 9 
- # Note - generics ->Very less code required as compare to mixin class, 
ListCreateAPIView - Concrete view for listing a queryset or creating a model instance.
https://www.django-rest-framework.org/api-guide/generic-views/

from rest_framework import generics
from .serializers import SubjectSerializer, TeacherSerializer
from core.models import Teacher,Subject

"""
Note - generics ->Very less code required as compare to mixin class,
- Here we need to create two classes oterwise if we keep in same class 2 arguments, issue will come
- 1 for primary key based operation 2nd class non-primary key based operations
- Solution is viewset - beacuse same code is being repeat in both classes
"""
#
class TeacherListview(generics.ListCreateAPIView):
    
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

"""get with pk, update, destroy"""
#
class TeacherDetailsview(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
#
class SubjectListview(generics.ListCreateAPIView):

    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()

"""get with pk, update, destroy"""
#
class SubjectDetailsview(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()

************************************
# Urls.py - Project app level

from django.contrib import admin
from django.urls import path
from Courses.views import TeacherListview, SubjectListview

#
urlpatterns = [
    path('teachers', TeacherListview.as_view()),
    path('teachers/<int:pk>', TeacherDetailsview.as_view()),
    path('subjects', SubjectListview.as_view()),
    path('subjects/<int:pk>', SubjectDetailsview.as_view())

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

==============================================

# Viewset - set of views is called viewset

# Issue in generics
- Need to map in urls.py 2 times
- Need to create 2 classes for primary key & non-primary key based operations
Solution:- Viewset
- Use Routers for url mapping
- Here we can make 1 class but 2 methods for primary key & non-primary key based operations
- 2 types - 1.View set 2. Model view set
- Here we need to overide mixin action mehtods like list(), retrive()
Drawback of viewset -
- For 1 class we need to write each method for for CURD operations -> more code
Solution - Model viewset
- No change in serializers


#
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

************************************
# Url mapping For Viewset -> using Router

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Courses.views import TeacherViewSet

#
router = DefaultRouter()
router.register('teachers',TeacherViewSet,basename='Teacher')

app_name = 'Courses'

urlpatterns = [
    path('', include(router.urls))
]

==============================================

# Model viewset- 

- only 2 lines of code and you will get all CURD operations methods
- No change in serializers

from rest_framework.viewsets import ModelViewSet
from .serializers import SubjectSerializer, TeacherSerializer
from core.models import Teacher,Subject

class TeacherViewSet(ModelViewSet):

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class SubjectViewSet(ModelViewSet):

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

************************************
# Url mapping For ModelViewset -> using Router

- No change in urls.py for model viewset , same as viewset


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Courses.views import TeacherViewSet,SubjectViewSet

router = DefaultRouter()
router.register('teachers',TeacherViewSet,basename='Teacher')
router.register('subjects',SubjectViewSet,basename='Subject')

app_name = 'Courses'

urlpatterns = [
    path('', include(router.urls))
]