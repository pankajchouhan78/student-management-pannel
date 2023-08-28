from django.contrib import admin
from . models import Courses , AddStudent, Teacher
# Register your models here.
admin.site.register(Courses)
admin.site.register(AddStudent)
admin.site.register(Teacher)