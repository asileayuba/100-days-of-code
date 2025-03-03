# Import necessary Django modules
from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Import models
from students.models import Student
from employees.models import Employee
from blogs.models import Blog, Comment

# Import serializers
from .serializers import StudentSerializer, EmployeeSerializer
from blogs.serializers import BlogSerializer, CommentSerializer

# Import Django REST framework components
from rest_framework.response import Response  # Handles API responses
from rest_framework import status  # Provides HTTP status codes
from rest_framework.decorators import api_view  # Allows defining API views that accept HTTP methods
from rest_framework.views import APIView
from rest_framework import mixins, generics, viewsets
from rest_framework.filters import SearchFilter

# Import pagination settings
from .paginations import CustomPagination

# Uncomment if needed
# from django.http import JsonResponse
from employees.filters import EmployeeFilter





@api_view(["GET", "POST"])
def studentsViews(request):
    if request.method == "GET":
        # Get all the data from the Student table
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # Storing Data Using Serializer
    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Define an API view that supports GET, PUT, and DELETE requests
@api_view(["GET", "PUT", "DELETE"])
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

    if request.method == "GET":
        # Serialize and return student data
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        # Update student details with validated request data
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        # Remove student record from the database
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# API view to handle employee-related requests
# class Employees(APIView):
#     def get(self, request):
#         # Retrieve all employee records from the database
#         employees = Employee.objects.all()

#         # Serialize the queryset to JSON format
#         serializer = EmployeeSerializer(employees, many=True)

#         # Return serialized data with a 200 OK status
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         # Deserialize and validate incoming employee data
#         serializer = EmployeeSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()  # Save the new employee record to the database
#             return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return the created employee data

#         # Return validation errors if data is invalid
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # API view to handle individual employee records
# class EmployeeDetail(APIView):

#     def get_object(self, pk):
#         """Retrieve an employee by primary key (pk) or raise 404 if not found."""
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             raise Http404  # Raise 404 error if employee does not exist

#     def get(self, request, pk):
#         """Handle GET request to retrieve a specific employee's details."""
#         employee = self.get_object(pk)  # Fetch the employee object
#         serializer = EmployeeSerializer(employee)  # Serialize the employee object
#         return Response(serializer.data, status=status.HTTP_200_OK)  # Return the serialized data

#     def put(self, request, pk):
#         """Handle PUT request to update an existing employee's details."""
#         employee = self.get_object(pk)  # Fetch the employee object
#         serializer = EmployeeSerializer(employee, data=request.data)  # Deserialize incoming data


#         if serializer.is_valid():
#             serializer.save()  # Save updated employee data
#             return Response(serializer.data, status=status.HTTP_200_OK)  # Return updated data

#         # Return validation errors if data is invalid
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         """Handle DELETE request to remove an employee record."""
#         employee = self.get_object(pk)  # Fetch the employee object
#         employee.delete()  # Delete the employee from the database
#         return Response(status=status.HTTP_204_NO_CONTENT)  # Return a 204 No Content response


# # Mixins
# # API view for listing all employees and creating a new employee
# class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()  # Define the queryset to retrieve all employees
#     serializer_class = EmployeeSerializer  # Specify the serializer for Employee model

#     def get(self, request):
#         """Handle GET request to list all employees."""
#         return self.list(request)  # Uses ListModelMixin to return all employee records

#     def post(self, request):
#         """Handle POST request to create a new employee record."""
#         return self.create(request)  # Uses CreateModelMixin to add a new employee


# # Mixins
# # API view for retrieving, updating, and deleting a specific employee
# class EmployeeDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()  # Define queryset to retrieve all employees
#     serializer_class = EmployeeSerializer  # Specify the serializer for Employee model

#     def get(self, request, pk):
#         """Handle GET request to retrieve details of a specific employee."""
#         return self.retrieve(request, pk)  # Uses RetrieveModelMixin

#     def put(self, request, pk):
#         """Handle PUT request to update an existing employee's details."""
#         return self.update(request, pk)  # Uses UpdateModelMixin

#     def delete(self, request, pk):
#         """Handle DELETE request to remove an employee record."""
#         return self.destroy(request, pk)  # Uses DestroyModelMixin


# # Generics
# # API view for listing all employees and creating a new employee
# class Employees(generics.ListCreateAPIView):
#     """
#     Handles GET requests to list all employees
#     and POST requests to create a new employee.
#     """
#     queryset = Employee.objects.all()  # Fetch all employee records
#     serializer_class = EmployeeSerializer  # Use EmployeeSerializer for data serialization


# # API view for retrieving, updating, and deleting a specific employee
# class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
#     """
#     Handles:
#     - GET request to retrieve an employee by primary key (pk).
#     - PUT request to update an existing employee.
#     - DELETE request to remove an employee record.
#     """
#     queryset = Employee.objects.all()  # Fetch all employee records
#     serializer_class = EmployeeSerializer  # Use EmployeeSerializer for data serialization
#     lookup_field = 'pk'  # Specify the lookup field for retrieving an employee


# ViewSet
# ViewSet for handling Employee operations
# class EmployeeViewSet(viewsets.ViewSet):
#     """
#     A simple ViewSet for listing and creating employees.
#     """

#     def list(self, request):
#         """
#         Handles GET request to retrieve all employee records.
#         """
#         queryset = Employee.objects.all()  # Fetch all employee records
#         serializer = EmployeeSerializer(queryset, many=True)  # Serialize the data
#         return Response(serializer.data)  # Return the serialized employee data

#     def create(self, request):
#         """
#         Handles POST request to create a new employee.
#         """
#         serializer = EmployeeSerializer(data=request.data)  # Deserialize request data
#         if serializer.is_valid():
#             serializer.save()  # Save new employee record
#             return Response(
#                 serializer.data, status=status.HTTP_201_CREATED
#             )  # Return created employee
#         return Response(
#             serializer.errors, status=status.HTTP_400_BAD_REQUEST
#         )  # Return validation errors

#     def retrieve(self, request, pk=None):
#         """
#         Handles GET request to retrieve an employee by primary key (pk).
#         """
#         employee = get_object_or_404(
#             Employee, pk=pk
#         )  # Retrieve employee or 404 if not found
#         serializer = EmployeeSerializer(employee)  # Serialize employee data
#         return Response(
#             serializer.data, status=status.HTTP_200_OK
#         )  # Return serialized employee data

#     def update(self, request, pk=None):
#         """
#         Handles PUT request to update an existing employee.
#         """
#         employee = get_object_or_404(
#             Employee, pk=pk
#         )  # Retrieve employee or 404 if not found
#         serializer = EmployeeSerializer(
#             employee, data=request.data
#         )  # Deserialize request data

#         if serializer.is_valid():
#             serializer.save()  # Save the updated employee data
#             return Response(
#                 serializer.data, status=status.HTTP_200_OK
#             )  # Return updated data
#         return Response(
#             serializer.errors, status=status.HTTP_400_BAD_REQUEST
#         )  # Return validation errors

#     def delete(self, request, pk=None):
#         """
#         Handles DELETE request to remove an employee by primary key (pk).
#         """
#         employee = get_object_or_404(
#             Employee, pk=pk
#         )  # Retrieve employee or 404 if not found
#         employee.delete()  # Delete the employee record
#         return Response(
#             status=status.HTTP_204_NO_CONTENT
#         )  # Return 204 No Content to confirm deletion



# ModelViewSet
# ViewSet for handling all CRUD operations on Employee model
class EmployeeViewSet(viewsets.ModelViewSet):
    """
    A ModelViewSet that provides full CRUD operations for the Employee model.

    - GET: Retrieve all employees or a specific employee by ID.
    - POST: Create a new employee record.
    - PUT/PATCH: Update details of an existing employee.
    - DELETE: Remove an employee record from the database.

    🔹 Additional Features:
    - Filtering: Supports filtering by 'designation'.
    - Pagination: Uses custom pagination for better data handling.
    - Ordering: Retrieves employees in ascending order based on 'id'.
    """
    
    queryset = Employee.objects.all().order_by('id')  # Fetch all employee records, ordered by ID
    serializer_class = EmployeeSerializer  # Defines the serializer for Employee data
    # pagination_class = CustomPagination  # Applies custom pagination settings
    filterset_class = EmployeeFilter  # Enables filtering employees by designation
    
    
    
    
    

# BLogs Views
# View for listing all blogs and creating a new blog
class BlogsView(generics.ListCreateAPIView):
    """
    Handles:
    - GET: Retrieve a list of all blogs.
    - POST: Create a new blog entry.
    """
    queryset = Blog.objects.all()  # Fetch all blog records
    serializer_class = BlogSerializer  # Use BlogSerializer for serialization


# View for listing all comments and creating a new comment
class CommentsView(generics.ListCreateAPIView):
    """
    Handles:
    - GET: Retrieve a list of all comments.
    - POST: Create a new comment entry.
    """
    queryset = Comment.objects.all()  # Fetch all comment records
    serializer_class = CommentSerializer  # Use CommentSerializer for serialization
    
    
class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a specific blog post by its primary key (pk).
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk' 


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a specific comment by its primary key (pk).
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk' 
