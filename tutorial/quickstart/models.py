'''from django.db import models
import email
from unicodedata import name

#student model

class student(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.IntegerField
    roll_number=models.CharField(max_length=20)
    phone_number=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"'''