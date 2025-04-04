from django import forms 
from .models import Account, UserProfile


class RegistrationForm(forms.ModelForm):
    """
    Form for user registration with additional password confirmation.
    """

    # Password input field with a placeholder and CSS class for styling
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control',
    }))

    # Confirm password input field with a placeholder and CSS class for styling
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'form-control',
    }))

    class Meta:
        """
        Meta class to specify the model and fields to include in the form.
        """
        model = Account  # Use the Account model
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']  # Fields to be displayed in the form

    def clean(self):
        """
        Custom validation to ensure that password and confirm_password match.
        """
        cleaned_data = super(RegistrationForm, self).clean()  # Get cleaned data from the form
        password = cleaned_data.get('password')  # Retrieve the password field
        confirm_password = cleaned_data.get('confirm_password')  # Retrieve the confirm password field

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Password does not match!")  # Raise validation error if passwords don't match

    def __init__(self, *args, **kwargs):
        """
        Customize form field attributes upon initialization.
        """
        super(RegistrationForm, self).__init__(*args, **kwargs)  # Call the parent constructor

        # Set placeholders for each field
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'

        # Apply a uniform CSS class to all fields for styling
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'phone_number')
    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        
        
class UserProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False, error_messages={'invalid':("Image Files Only")}, widget=forms.FileInput())
    class Meta:
        model = UserProfile
        fields = ('address_line_1', 'address_line_2', 'city', 'state', 'country', 'profile_picture')   
        
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'