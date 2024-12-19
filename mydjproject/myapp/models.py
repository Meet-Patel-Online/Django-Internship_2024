from django.db import models

# Create your models here.
class student(models.Model):
    sname=models.CharField("Name",max_length=50,blank=False)
    semail = models.CharField("Email",max_length=50)
    spassword = models.CharField("password",max_length=50)
    createAT = models.DateTimeField("created",auto_now_add=True)
    
def __str__(self):
    return self.sname
