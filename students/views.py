from django.shortcuts import render

# students/views.py

from rest_framework import viewsets
from .models import Student
from .SERIALIZER import StudentSerializer
from rest_framework import generics
from .models import Student

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


'''class StudentCreateView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer'''




# Create your views here.
