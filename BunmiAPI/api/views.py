from django.shortcuts import render
from rest_framework import generics
from .serializers import StudentSerializer
from .models import Student

# Create your views here.
class StudentGetAPI(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentPostAPI(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentPutAPI(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer  

class StudentDeleteAPI(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer      