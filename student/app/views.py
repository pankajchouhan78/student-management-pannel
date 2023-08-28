from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.db.models import Q
from .models import *


# Create your views here.
def home(request):
    return render(request,"index.html")

def dashboard(request):
    count_student = AddStudent.objects.all().count()
    courses = Courses.objects.all()
    count_course = courses.count()

    context = {
        'Courses':courses,
        'count_student':count_student,
        'count_course':count_course,
    }
    return render(request,"dashboard.html",context)

def signup(request):
    return render(request,"sign-up.html")

def registration(request):
    if request.method == "POST":
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = make_password(request.POST.get('name'))

        if User.objects.filter(username = username).exists():
            messages.error(request , "Username already exists")
            return redirect('/signup/')
        else:
            User.objects.create(
                name = name,
                username = username,
                password = password,
            )
            return redirect('/') # index


def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        user_password = request.POST.get('password')

        print(username, user_password)

        if User.objects.filter(username = username).exists():
            obj = User.objects.get(username = username)
            password = obj.password
            if check_password(user_password, password):
                return redirect('/dashboard/')
            else:
                messages.error(request,"Invalid Password")
                return redirect('/')
        else:
            messages.error(request,"Invalid Username")
            return redirect('/')


def cources(request):
    courses = Courses.objects.all()
    context = {
        'courses':courses,
    }
    return render(request,"courses/courses.html",context)

def add_courses(request):
    if request.method == "POST":
        courses_name = request.POST.get('courses')
        duration = request.POST.get('duration')
        fees = request.POST.get('fees')
        # print(courses_name,duration,fees)


        if Courses.objects.filter(courses_name = courses_name).exists():
            messages.error(request, f"{courses_name} are already exists")
            return redirect('/courses/')
        else:  
            courese_obj=Courses.objects.create(
                courses_name = courses_name,
                duration = duration,
                fees = fees,
            )
            # print(courese_obj)
            messages.success(request,f"{courses_name} are successfully added")
            return redirect('/courses/')
        
def update_course(request, id):
    if request.method == "POST":
        cname = request.POST.get('course_name')
        duraion = request.POST.get('duration')
        fees = request.POST.get('fees')

        course = Courses.objects.filter(id = id).update(
            courses_name = cname,
            duration  = duraion,
            fees = fees,
        )
        messages.success(request, "Course successfully updated")
        return redirect('/courses/')
    else:
        course = Courses.objects.get(id = id)
        context = {
            'courses':course,
        }
    return render(request,"courses/course_update.html",context)

def delete_course(request, id):
    course = Courses.objects.filter(id = id)
    course.delete()
    messages.success(request, "Course successfully deleted")
    return redirect('/courses/')

def course_search(request):
    if 'search' in request.GET:
        course = request.GET.get('search')
        print(course)
        multi_q = Q(Q(courses_name__icontains = course))
        coursee = Courses.objects.filter(multi_q)
        context = {
            'courses':coursee,
        }
    else:
        course = Courses.objects.all()
        context = {
            'courses':course,
        }
    return render(request, "courses/courses.html",context)



def student_search(request):  
    if 'search' in request.GET:
            search = request.GET['search']
            multiple_q = Q(Q(sname__icontains = search) | Q(collage__icontains = search))
            student = AddStudent.objects.filter(multiple_q)
            context = {
                'Students':student,
            }
    else:
        student = AddStudent.objects.all()
        courses = Courses.objects.all()
        context = {
            'Students':student,
        }
    return render(request, "students/viewstudents.html",context)

def viewstudent(request):
        student = AddStudent.objects.all()
        courses = Courses.objects.all()
        context = {
            'Students':student,
            'courses':courses,
        }
        return render(request, "students/viewstudents.html",context)

def add_student(request):
    if request.method =="POST":
        data= request.POST
        name = data.get('sname')
        email = data.get('email')
        mobile = data.get('number')
        collage = data.get('collage')
        degree= data.get('degree')
        courses_id= data.get('course')
        address = data.get('address')
        total_amount = data.get('tatol_amount')
        paid_amount = data.get('paid_amount')

        course = Courses.objects.get(id = courses_id)

        AddStudent.objects.create(
            sname = name,
            semail = email,
            smobile = mobile,
            collage = collage,
            sdegree = degree,
            scourse = course,
            saddress = address,
            total_amount = total_amount,
            paid_amount = paid_amount,
        )
        messages.success(request, name + " are successfully added")
        return redirect('/viewStudent/')
    
def update_student(request, id):
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        mobile = data.get('mobile')
        degree = data.get('degree')
        course_id = data.get('course')
        paid_amount = data.get('paid_amount')
        address = data.get('address')

        student = AddStudent.objects.filter(id = id ).update(
            sname= name,
            semail = email,
            smobile = mobile,
            saddress = address,
            sdegree = degree,
        )
        

        if paid_amount != None and paid_amount != "":
            student.paid_amount = paid_amount
            AddStudent.calculate_due_amount()
        student.save()
        messages.success(request, "Student successfully updated")
        return redirect('/viewStudent/')
        
    student = AddStudent.objects.get(id = id)
    course = Courses.objects.all()
    context = {
        'Courses': course,
        'Student': student,
    }
    return render(request,"students/update_student.html",context)

def student_profile(request, id):
    student = get_object_or_404(AddStudent, id=id)
    context = {
        'Student':student,
    }
    return render(request, "students/student_profile.html",context)




def viewTeacher(request):
    student = AddStudent.objects.all()
    courses = Courses.objects.all()
    teacher = Teacher.objects.all()
    context = {
        'Students':student,
        'courses':courses,
        'Teachers':teacher,
    }
    return render(request,"teachers/viewTeacher.html",context)

def teacher_search(request):
    if 'search' in request.GET:
        name = request.GET['search']
        # print(name)
        multiple_q = Q(Q(teachername__icontains = name) | Q(education__icontains = name))
        teacher = Teacher.objects.filter(multiple_q)
        context = {
            'Teachers':teacher,
        }
    else:
        teacher = Teacher.objects.all()
        context = {
            'Teachers':teacher,
        }
    return render(request,"teachers/viewTeacher.html",context)
   
# def index(request):
#     if "q" in request.GET:
#         q = request.GET["q"]
#         multiple_q = Q(Q(sname__icontains=q) | Q(semail__icontains=q)) | Q(
#             smobile__icontains=q
#         )
#         stu = AddStudents.objects.filter(multiple_q)
#     else:
#         stu = AddStudents.objects.all()
#     context = {"stu": stu}
#     return render(request, "hrm/viewstudents.html", context)


def add_teacher(request):
    if request.method == "POST":
        data = request.POST
        teachername = data.get('tname')
        teacher_id = data.get('tid')
        teacheremail = data.get('email')
        teacherpassword = data.get('password')
        teachermobile = data.get('mobile')
        education = data.get('education')
        workexp = data.get('workshop')
        photo = request.FILES.get('myfile')
        student = data.get('student') 
        teachercourse= data.get('course')
        gender = data.get('gender') 

        if Teacher.objects.filter(employeesid = teacher_id).exists():
            messages.error(request,"Teacher already exists")
            return redirect('/viewTeacher/')

        course = Courses.objects.get(id = teachercourse)
        studentt = AddStudent.objects.get(id = student)
        password = make_password(teacherpassword)
        
        Teacher.objects.create(
            teachername = teachername,
            employeesid = teacher_id,
            teacheremail = teacheremail,
            teachermobile = teachermobile,
            education = education,
            workexp = workexp,
            photo =  photo,
            gender = gender,
            student = studentt,
            teachercourse = course,
            teacherpassword = password,
        )
        messages.success(request,f"{teachername} are successfull added")
        return redirect('/viewTeacher/')
    
def updateTeacher(request,id):
    if request.method =="POST":
        data = request.POST
        teachername = data.get('tname')
        teacher_id = data.get('tid')
        teacheremail = data.get('email')
        teachermobile = data.get('mobile')
        education = data.get('education')
        workexp = data.get('workshop')
        photo = request.FILES.get('myfile')
        student = data.get('student') 
        teachercourse= data.get('course')
        gender = data.get('gender') 
        password = make_password(data.get('password'))

        course = Courses.objects.get(id = teachercourse)
        studentt = AddStudent.objects.get(id = student)
        teacher = Teacher.objects.filter(id = id)

        t1 = Teacher.objects.get(id = id)
        if password != None and password!="":
                t1.teacherpassword = password

        if photo != None and photo != "":
            t1.photo = photo

        t1.save()

        teacher.update(
            teachername = teachername,
            employeesid = teacher_id,
            teacheremail = teacheremail,
            teachermobile = teachermobile,
            education = education,
            workexp = workexp,
            gender = gender,
            student = studentt,
            teachercourse = course,
        )
        messages.success(request,f"{teachername} are  Updated")
        return redirect('/viewTeacher/')
    
    else:
        student = AddStudent.objects.all()
        courses = Courses.objects.all() 
        teacher = Teacher.objects.get(id = id)
        context = {
            'Teachers':teacher,
            'Students':student,
            'courses':courses,
        }
        return render(request,'teachers/update_teacher.html',context)
    
def teacher_profle_view(request, id):
    teacher = get_object_or_404(Teacher, id = id )
    context = {
        'Teacher':teacher,
    }
    return render(request, "teachers/teacher_profle_view.html",context)

    