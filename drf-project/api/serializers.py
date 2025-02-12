from rest_framework import serializers
from students.models import Student
from employees.models import Employee

# Serializer for the Student model
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student  # Specify the model to serialize
        fields = "__all__"  # Include all model fields in the serialized output
        
# Serializer for the Employee model
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee  # Specify the model to serialize
        fields = "__all__"  # Include all model fields in the serialized output
