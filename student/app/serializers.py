from .models import *
from rest_framework import serializers

class Courseserializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'

class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model = AddStudent
        fields = '__all__'

class ParticuartfieldStudentserializer(serializers.ModelSerializer):
    class Meta:
        model = AddStudent
        fields = ['sname','smobile']


