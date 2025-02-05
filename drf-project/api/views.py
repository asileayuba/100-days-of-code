from django.shortcuts import render
from django.http import JsonResponse



def studentsViews(request):
    students = {
        'id': 1,
        'name': 'Asile',
        'class': 'Computer Science'
    }
    return JsonResponse(students)
