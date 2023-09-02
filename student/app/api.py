from .models import *
from .serializers import *
from rest_framework import generics
from django.shortcuts import render

class CourseViewSet(generics.CreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = Courseserializer

class CourseListViewSet(generics.ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = Courseserializer

class CourseRetriveViewSet(generics.RetrieveAPIView):
    queryset = Courses.objects.all()
    serializer_class = Courseserializer

class CourseDEleteViewSet(generics.DestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = Courseserializer


# Student
class StudentViewSet(generics.CreateAPIView):
    queryset = AddStudent.objects.all()
    serializer_class = Studentserializer

class StudentlistView(generics.ListAPIView):
    queryset = AddStudent.objects.all()
    serializer_class = Studentserializer

class StudentRetrive(generics.RetrieveAPIView):
    queryset = AddStudent.objects.all()
    serializer_class = Studentserializer

class StudentDelete(generics.DestroyAPIView):
    queryset = AddStudent.objects.all()
    serializer_class = Studentserializer

class StudentUpdate(generics.UpdateAPIView):
    queryset = AddStudent.objects.all()
    serializer_class = Studentserializer

class StudentSomeFieldUpdate(generics.UpdateAPIView):
    queryset = AddStudent.objects.all()
    serializer_class = ParticuartfieldStudentserializer

class StudentDelete(generics.DestroyAPIView):
    queryset = AddStudent.objects.all()
    serializer_class = Studentserializer

class StudentListCreate(generics.ListCreateAPIView): # it will create student and list student
    queryset = AddStudent.objects.all()
    serializer_class = Studentserializer

class StudentRetriveUpdate(generics.RetrieveUpdateAPIView): # it will list student and update student
    queryset = AddStudent.objects.all()
    serializer_class = Studentserializer