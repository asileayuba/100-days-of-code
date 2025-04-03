from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Custom user manager to handle user and superuser creation
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        """
        Creates and returns a standard user.
        
        - Ensures email and username are provided.
        - Normalizes the email.
        - Sets the user password securely.
        """
        if not email:
            raise ValueError('User must have an email address')
        
        if not username:
            raise ValueError('User must have a username')
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        
        user.set_password(password)  # Hashes and sets the password
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        """
        Creates and returns a superuser.
        
        - Assigns admin privileges.
        - Ensures the user is active and staff.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user
    

# Custom user model
class Account(AbstractBaseUser):
    """
    Custom user model that replaces Django's default user system.
    
    Fields:
    - first_name, last_name, username, email (unique), phone_number.
    - Authentication-related fields: date_joined, last_login, is_admin, is_staff, is_active, is_superadmin.

    Features:
    - Uses email as the primary login identifier.
    - Includes custom user permissions.
    - Managed via `MyAccountManager`.
    """
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)
    
    # Required authentication fields
    date_joined = models.DateTimeField(auto_now_add=True)  # Automatically sets on user creation
    last_login = models.DateTimeField(auto_now_add=True)  # Updates on each login
    is_admin = models.BooleanField(default=False)  # Admin users
    is_staff = models.BooleanField(default=False)  # Staff members
    is_active = models.BooleanField(default=False)  # Active user status
    is_superadmin = models.BooleanField(default=False)  # Superuser privileges
    
    USERNAME_FIELD = 'email'  # Login identifier
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']  # Additional required fields
    
    objects = MyAccountManager()  # Attach custom manager
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return self.email  # Returns email when object is printed
    
    def has_perm(self, perm, obj=None):
        """Grant all permissions to admin users."""
        return self.is_admin
    
    def has_module_perms(self, add_label):
        """Allow access to all app modules for admin users."""
        return True


class UserProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    address_line_1 = models.CharField(blank=True, max_length=100)
    address_line_2 = models.CharField(blank=True, max_length=100)
    profile_pic = models.ImageField(blank=True, upload_to='userprofile/')
    city = models.CharField(blank=True, max_length=20)
    state = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)
    
    def __str__(self):
        return self.user.first_name
    
    def full_address(self):
        return f"{self.address_line_1} {self.address_line_2}"