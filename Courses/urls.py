# from django.urls import path, include
# from rest_framework.routers import DefaultRouter

# from Courses import views

# router = DefaultRouter()
# router.register('teachers',views.TeacherListview)

# app_name = 'Courses'

# urlpatterns = [
#     path('', include(router.urls))
# ]

from django.contrib import admin
from django.urls import path
from Courses.views import *

urlpatterns = [
    path('teachers', TeacherListview.as_view()),
    path('teachers/<int:pk>', TeacherDetailsview.as_view()),
    path('subjects', SubjectListview.as_view()),
    path('subjects/<int:pk>', SubjectDetailsview.as_view())


]