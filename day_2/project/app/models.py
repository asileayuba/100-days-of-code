from django.db import models

# models for Contact page
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=12)
    description = models.TextField()
    # to display name of person that submit a form in my admin dashboard
    def __str__(self):
        return f"Message from {self.name}"

# models for Blog page
class Blogs(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    authname=models.CharField(max_length=50)
    img=models.ImageField(upload_to='pics', blank=True, null=True)
    timeStamp=models.DateTimeField(auto_now_add=True)
    # to display name of author that published the content in admin dashboard
    def __str__(self):
        return f"Uploaded by {self.authname}"