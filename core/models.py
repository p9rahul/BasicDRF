from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    #this method returns a human-readable string representation of an object in DB 
    def __str__(self):
        return self.email
    
class Subject(models.Model):
    title = models.CharField(max_length=20)
    rating = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='Subjects')

'''
select * from [dbo].[core_subject]

select * from [dbo].[core_teacher]

select * from [dbo].[core_subject] sub
right JOIN [dbo].[core_teacher] tec
on sub.teacher_id = tec.id
where tec.name='john'
'''