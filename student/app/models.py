from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Courses(models.Model):
    courses_name = models.CharField(max_length=250 , unique=True)
    duration = models.CharField( max_length=100)
    fees = models.FloatField()

    def __str__(self):
        return self.courses_name
    
class AddStudent(models.Model):
    sname= models.CharField(max_length=100, blank=True, null=True)
    semail = models.EmailField(max_length=254)
    smobile = models.CharField(max_length=10)
    saddress = models.CharField(max_length=255)
    collage = models.CharField(max_length=100 , default="")
    sdegree = models.CharField(max_length=100)
    total_amount = models.IntegerField()
    paid_amount = models.IntegerField()
    due_amount = models.FloatField(default=0)
    scourse= models.ForeignKey(Courses, on_delete=models.CASCADE)

    def calculate_due_amount(self):
        if self.due_amount ==0:
            self.due_amount = self.total_amount - self.paid_amount
            return self.due_amount
        else:
            self.paid_amount += self.due_amount
            self.due_amount = self.total_amount - self.paid_amount
            return self.due_amount  


    def __str__(self):
        return self.sname


GENDER_CHOICE = (
    {'M', 'Male'},
    {'F', 'Female'},
    {'O', 'Other'},
)
class Teacher(models.Model):
    teachername=models.CharField(max_length=300)
    employeesid = models.IntegerField(unique=True, default=0)
    teacheremail=models.CharField(max_length=200,unique=True)
    teacherpassword=models.CharField(max_length=300)
    teachermobile=models.IntegerField()
    joindate=models.DateField(auto_now_add=True)
    education=models.CharField(max_length=100)
    workexp=models.CharField(max_length=200)
    photo = models.ImageField(upload_to="teachers/")
    student = models.ForeignKey(AddStudent, on_delete=models.CASCADE)                          
    teachercourse=models.ForeignKey(Courses , on_delete=models.CASCADE)  
    gender = models.CharField(choices=GENDER_CHOICE , max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.teachername


    