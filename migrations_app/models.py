from django.db import models
from django.urls import reverse

class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'migrations_app'

class Student(models.Model):
    name = models.CharField(max_length=250)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    # class Meta: 
    #     indexes = [
    #         models.Index(fields=['name'], name='student_name_idx')
    #     ]
    
    class Meta: 
        app_label = 'migrations_app'