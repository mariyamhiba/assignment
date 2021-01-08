from django.db import models

# Create your models here.
class user_login(models.Model):
    # id
    uname = models.CharField(max_length=50)
    password = models.CharField(max_length=25)
    utype = models.CharField(max_length=10)
    def __str__(self):
        return self.uname


class user(models.Model):
    # id
    uname = models.CharField(max_length=50)
    rollno = models.IntegerField()
    course= models.CharField(max_length=10)
    def __str__(self):
        return self.uname


class student_details(models.Model):
    sname= models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    def __str__(self):
        return self.sname

