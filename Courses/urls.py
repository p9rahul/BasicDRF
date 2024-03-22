'''
# use for generics-
 
from django.contrib import admin
from django.urls import path
from Courses.views import *

urlpatterns = [
    path('teachers', TeacherListview.as_view()),
    path('teachers/<int:pk>', TeacherDetailsview.as_view()),
    path('subjects', SubjectListview.as_view()),
    path('subjects/<int:pk>', SubjectDetailsview.as_view())
]
'''

# For Viewset
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