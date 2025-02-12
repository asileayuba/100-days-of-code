from django.db import models

# Employee model representing employee details
class Employee(models.Model):
    emp_id = models.CharField(max_length=20)  # Unique employee ID
    emp_name = models.CharField(max_length=50)  # Employee's full name
    designation = models.CharField(max_length=50)  # Job role or title

    def __str__(self):
        return self.emp_name  # Return employee name as the string representation
