from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    roll_no=models.CharField(max_length=10)
    phone_number=models.CharField(max_length=10)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


