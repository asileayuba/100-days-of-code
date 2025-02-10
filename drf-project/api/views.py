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
    
    
# Define an API view that only accepts GET requests
@api_view(['GET'])
def studentDetailView(request, pk):
    """
    Retrieve a student's details by primary key (pk).
    Returns 404 if the student does not exist.
    """
    try:
        # Attempt to retrieve the student object by primary key (pk)
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        # If the student is not found, return a 404 Not Found response
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # If the request method is GET, serialize the student object and return the data
    if request.method == 'GET':
        serializer = StudentSerializer(student)  # Convert student object to JSON format
        return Response(serializer.data, status=status.HTTP_200_OK)  # Return the serialized data
    
    elif request.method == 'PUT':
        serializer = StudentSerializer(data=request.data)