from django.urls import path
from . import views
from .api import *

urlpatterns = [
    path('',views.home),
    
    path('signup/',views.signup,name="signup"),
    path('register/',views.registration,name="register"),
    path('signin/',views.signin,name="signin"),                 # banana hai

    path('dashboard/',views.dashboard,name="dashboard"),
    
    path('courses/',views.cources,name="courses"),
    path('add_courses/',views.add_courses,name="add_courses"),
    path('update_course/<int:id>/',views.update_course,name="update_course"),
    path('delete_course/<int:id>/',views.delete_course,name="delete_course"),
    path('course_search/',views.course_search,name="course_search"),

    path('viewStudent/',views.viewstudent,name="viewStudent"),
    path('add_student/',views.add_student,name="add_student"),
    path('update_student/<int:id>/',views.update_student,name="update_student"),
    path('student_profile/<int:id>/',views.student_profile,name="student_profile"),

    path('viewTeacher/',views.viewTeacher,name="viewTeacher"),
    path('add_teacher/',views.add_teacher,name="add_teacher"),
    path('updateTeacher/<int:id>/',views.updateTeacher,name="updateTeacher"),
    path('teacher_profle_view/<int:id>/',views.teacher_profle_view,name="teacher_profle_view"),


    path('teacher_search/',views.teacher_search,name="teacher_search"),
    path('student_search/',views.student_search,name="student_search"),

    path('course_create/',CourseViewSet.as_view()),
    path('course_listview/',CourseListViewSet.as_view()),
    path('course_restrive/<int:pk>/',CourseRetriveViewSet.as_view()),
    path('course_delete/<int:pk>/',CourseDEleteViewSet.as_view()),


    # for student
    path('student_create_view_set/',StudentViewSet.as_view()),
    path('student_list_view/',StudentlistView.as_view()),
    path('student_retrive/<int:pk>/',StudentRetrive.as_view()),
    path('student_delete/<int:pk>/',StudentDelete.as_view()),
    path('student_some_update/<int:pk>/',StudentSomeFieldUpdate.as_view()),

    path('student_list_create/',StudentListCreate.as_view()),
    path('student_list_update/<int:pk>/',StudentRetriveUpdate.as_view()),
    

]