from django.db import models

# Create your models here.
class Student(models.Model):
    stuname = models.CharField(max_length=50)
    stuemail = models.EmailField()
    stuphone = models.IntegerField()
