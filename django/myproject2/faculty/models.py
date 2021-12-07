from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=40)
    email= models.EmailField(max_length=35)
    complaint=models.CharField(max_length=1000)
    gender=[("male","male"),("female","female")]
    usergender= models.CharField(max_length=10,choices=gender)

    def __str__(self):
        return self.name

    
class Registration(models.Model):
    name=models.CharField(max_length=40)
    age= models.IntegerField()
    gen=[('male','male'),('female','female')]
    gender= models.CharField(max_length=10,choices=gen)
    experience=models.CharField(max_length=15)
    specialization=models.CharField(max_length=20)
    Qualification=models.CharField(max_length=25)
    email= models.EmailField(max_length=50)
    address= models.CharField(max_length=50)
    phonenumber= models.CharField(max_length=10)
    username= models.CharField(max_length=20)
    password=models.CharField(max_length=20)


    def __str__(self):
        return self.name, self.Qualification,self.specialization

    
class ImgLoad(models.Model):
    name= models.CharField(max_length=30)
    img= models.ImageField(upload_to="storImg/",null=True,default="profile.png")


class Employee(models.Model):
    salary=models.FloatField()
    user=models.OneToOneField(Registration,on_delete=models.CASCADE)