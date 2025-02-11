# Import necessary decorators and modules

# from django.shortcuts import render
# from django.http import JsonResponse
from students.models import Student # Import the Student model 
from .serializers import StudentSerializer # Import the serializer for the Student model
from rest_framework.response import Response # Handles API responses
from rest_framework import status # Provides HTTP status codes
from rest_framework.decorators import api_view  # Allows defining API views that accept HTTP methods


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
