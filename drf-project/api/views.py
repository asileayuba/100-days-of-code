from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student


def studentsViews(request):
    students = Student.objects.all()
    # Manual Serialization
    students_list = list(students.values())
    return JsonResponse(students_list, safe=False)
