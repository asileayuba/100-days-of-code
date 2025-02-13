# Import necessary decorators and modules

# from django.shortcuts import render
# from django.http import JsonResponse
from students.models import Student # Import the Student model 
from .serializers import StudentSerializer, EmployeeSerializer # Import the serializer for the Student and Employee model
from rest_framework.response import Response # Handles API responses
from rest_framework import status # Provides HTTP status codes
from rest_framework.decorators import api_view  # Allows defining API views that accept HTTP methods
from rest_framework.views import APIView
from employees.models import Employee

@api_view(['GET', 'POST'])
def studentsViews(request):
    if request.method == 'GET':
        # Get all the data from the Student table
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # Storing Data Using Serializer
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
# Define an API view that supports GET, PUT, and DELETE requests
@api_view(['GET', 'PUT', 'DELETE'])
def studentDetailView(request, pk):
    """
    Retrieve, update, or delete a student by primary key (pk).
    Returns 404 if the student does not exist.
    """
    try:
        # Fetch student by primary key (pk); return 404 if not found
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        # Serialize and return student data
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        # Update student details with validated request data
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        # Remove student record from the database
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# API view to handle employee-related requests
class Employees(APIView):
    def get(self, request):
        # Retrieve all employee records from the database
        employees = Employee.objects.all()
        
        # Serialize the queryset to JSON format
        serializer = EmployeeSerializer(employees, many=True)
        
        # Return serialized data with a 200 OK status
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    