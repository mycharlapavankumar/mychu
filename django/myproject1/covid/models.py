from django.db import models

# Create your models here.
class Patients(models.Model):
    p_name=models.CharField(max_length=20,null=False)
    p_age=models.IntegerField(null=False)
    p_email=models.EmailField(null=False)

    def __str__(self):
        return self.p_name

class student(models.Model):
    s_name= models.CharField(max_length=30,null=False)
    s_age= models.IntegerField(null=False)
    s_phone= models.IntegerField(null=False)
    s_email=models.EmailField()
    s_rollno=models.CharField(max_length=10,null=False)
    s_gender=models.CharField(max_length=10,null=False)
    s_add=models.CharField(max_length=50)
    s_uname=models.CharField(max_length=20,null=False)
    s_pass= models.CharField(max_length=20,null=False)

    def __str__(self):
        return self.s_uname
        
