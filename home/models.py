from django.db import models



# Create your models here.

class Student(models.Model):
    #id=models.AutoField()
    student_name=models.CharField('Student Name',max_length=30,null=True)
    dept=(
        ('ise','info science'),
        ('mh','mech'),
        ('cv','civil'),
        ('bt','biotech')
    )
    sec=(
        ('a','A'),('b','B'),('c','C')
    )
    photo=models.ImageField(upload_to='static/img/1.jpg')
    department=models.CharField('Department',choices=dept,blank=True,null=True,max_length=30)
    timestamp=models.DateTimeField(auto_now_add=True)
    section=models.CharField('Section',choices=sec,blank=True,null=True,max_length=10)
    def __str__(self):
        return self.student_name

    
class Library(models.Model):
    #sut=models.ForeignKey('Student',on_delete=models.SET_NULL,null=True)
    #sut=models.ForeignKey('Student',on_delete=models.CASCADE)
    libraby_name=models.CharField('Library',null=True,max_length=100)
    #b=(('hp','harry potter'),('p','python'),('a','alice'))
    books=models.ManyToManyField('Book',null=True)
    #time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.libraby_name

class Book(models.Model):
    book=models.CharField('Book',max_length=100,null=True)
    def __str__(self):
        return self.book

class Sectionn(models.Model):
    sectionn=models.CharField('Sectionn',max_length=20,null=False)
    advisor=models.OneToOneField('Teacher',on_delete=models.SET_NULL,null=True)
    students=models.ManyToManyField('Student',null=False)
    def __str__(self):
        return self.sectionn

class Teacher(models.Model):
    teacher=models.CharField('Teacher Name',max_length=100,null=False)
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.teacher