# 100 Days of Code: Day 2

## Learning Django Basics

Today, I dived into the basics of Django, focusing on setting up and understanding the framework's core components. Below is a summary of what I accomplished:

### Key Learnings
- **Setting up a Django Project**: 
  - Installed Django in a virtual environment.
  - Created a new Django project using the `django-admin startproject` command.
  
- **Explored the `settings.py` File**:
  - Understood its structure and the role of important settings like `INSTALLED_APPS`, `DATABASES`, and `TEMPLATES`.

- **Created a Basic App**:
  - Used the `python manage.py startapp` command to create an app.
  - Learned how to register the app in the `INSTALLED_APPS` list.

- **Running the Development Server**:
  - Started the server using `python manage.py runserver`.
  - Tested the default Django welcome page and customized URLs for new views.

- **Worked with Django Templates**:
  - Practiced rendering templates using the `render` function.
  - Created a simple HTML file and learned how to use Django's template engine.

---

### Code and Files
You can find the code and exercises from today's session in this [day_2](./day_2) folder of this repository.

---

### Challenges and Insights
- Setting up the `settings.py` file helped me understand how Django handles project configurations.
- Practicing template rendering gave me insights into how Django dynamically generates web pages.

---

### Resources
- [Django Documentation](https://docs.djangoproject.com/en/)
- YouTube Channel: [The Ark Pro Coder](https://www.youtube.com/@ARKPROCODER)

---

Stay tuned for Day 3!



# 100 Days of Code: Day 3

## Bootstrap Integration in Django Website

Today, I focused on integrating Bootstrap into my Django website. Below is a summary of what I accomplished:

### Key Learnings
- **Installed Bootstrap**:
  - Added Bootstrap to the project by linking the CDN in the HTML `<head>` section.
  
- **Integrated Bootstrap Styles**:
  - Applied Bootstrap's grid system and components to the existing HTML files.
  - Improved the layout of the homepage by using Bootstrap's container, row, and column classes.
  - Styled the navbar, form inputs, and buttons using Bootstrap classes.

- **Enhanced User Interface**:
  - Customized the carousel component using Bootstrap's carousel classes.
  - Incorporated a spinner that is displayed directly under the carousel images to indicate loading.

- **Responsive Design**:
  - Ensured the website layout is responsive by using Bootstrap's responsive grid system and utility classes for better mobile support.

---

### Code and Files
You can find the code and exercises from today's session in this [day_2](./day_2) folder of this repository.

---

### Challenges and Insights
- Bootstrap's integration was straightforward using the CDN, but customizing certain components like the carousel required understanding its structure and JavaScript behavior.
- I learned how to make the page layout responsive and visually appealing with minimal effort using Bootstrap's built-in classes.

---

### Resources
- [Bootstrap Documentation](https://getbootstrap.com/)
- [Django Documentation](https://docs.djangoproject.com/en/)
- YouTube Channel: [The Ark Pro Coder](https://www.youtube.com/@ARKPROCODER)

---

Stay tuned for Day 4!



# 100 Days of Code: Day 4

## Exploring Jinja in Django Templates and Bootstrap Forms

Today, I explored Django's template system and utilized its Jinja-inspired syntax for creating dynamic and reusable templates. Additionally, I used Bootstrap to design a user-friendly signup and login page. Below is a summary of what I accomplished:

### Key Learnings
- **Django Template System**:
  - Gained a deeper understanding of template inheritance, blocks, and the `extends` keyword.
  - Learned how to use `for` loops and conditional statements within templates to dynamically render content.

- **Bootstrap Forms**:
  - Styled signup and login pages with Bootstrap components.
  - Enhanced user experience using Bootstrap classes for inputs, buttons, and form layouts.
  - Implemented responsive designs to ensure compatibility across devices.

---

### Code and Files
You can find the code and exercises from today's session in this [day_2](./day_2) folder of this repository.

---

### Challenges and Insights
- Template inheritance streamlined the process of maintaining consistent layouts across multiple pages.
- Using Bootstrap for forms made styling and layout adjustments faster and more efficient.

---

### Resources
- [Bootstrap Documentation](https://getbootstrap.com/)
- [Django Documentation](https://docs.djangoproject.com/en/)
- YouTube Channel: [The Ark Pro Coder](https://www.youtube.com/@ARKPROCODER)

---

Stay tuned for Day 5!



# 100 Days of Code: Day 5

## Django Authentication System for Signup Page

Today, I implemented the backend functionality for the signup page using Django's built-in authentication system. Below is a summary of what I accomplished:

### Key Learnings
- **Django Authentication Framework**:
  - Learned to use Django's built-in `User` model for handling user registrations.
  - Configured views to handle user input and validate registration data.

- **Signup Page Functionality**:
  - Connected the signup form to the backend for creating new users.
  - Added input validation to ensure email uniqueness and password strength.
  - Displayed success or error messages to guide users during registration.

- **Error Handling**:
  - Used Django's `messages` framework to notify users about the registration status.
  - Managed edge cases like duplicate emails or missing required fields.

---

### Code and Files
You can find the code and exercises from today's session in this [day_2](./day_2) folder of this repository.

---

### Challenges and Insights
- Integrating the backend with the frontend provided a complete flow from user input to account creation.
- Handling errors gracefully improved the user experience.

---

### Resources
- [Django Documentation](https://docs.djangoproject.com/en/)
- [Bootstrap Documentation](https://getbootstrap.com/)
- YouTube Channel: [The Ark Pro Coder](https://www.youtube.com/@ARKPROCODER)

---

Stay tuned for Day 6!


# 100 Days of Code: Day 6

## Django Alert Messages Integration

Today, I focused on integrating Django's alert messages framework into my project to enhance user feedback and provide clear notifications. Below is a summary of what I accomplished:

### Key Learnings
- **Django Messages Framework**:
  - Configured Django's `messages` framework to display alerts for success, error, and info events.
  - Used the `messages.add_message`, `messages.success`, `messages.error`, and other methods to define feedback messages.

- **Integrating Alerts into Templates**:
  - Rendered alert messages in templates using the `for` loop and Bootstrap classes for styling.
  - Ensured messages appear dynamically based on user actions like login, signup, or form submission.

- **Bootstrap Styling for Alerts**:
  - Applied Bootstrap alert classes (`alert-success`, `alert-danger`, `alert-info`, etc.) for consistent and visually appealing notifications.
  - Customized alert designs to align with the overall theme of the project.

---

### Code and Files
You can find the code and exercises from today's session in this [day_2](./day_2) folder of this repository.

---

### Challenges and Insights
- Implementing alert messages improved user experience by providing immediate feedback on actions.
- Combining Django's messages framework with Bootstrap styling ensured a professional and user-friendly interface.

---

### Resources
- [Django Messages Framework Documentation](https://docs.djangoproject.com/en/stable/ref/contrib/messages/)
- [Bootstrap Alerts Documentation](https://getbootstrap.com/docs/5.1/components/alerts/)
- YouTube Channel: [The Ark Pro Coder](https://www.youtube.com/@ARKPROCODER)

---

Stay tuned for Day 7!


# 100 Days of Code: Day 7

## Django Login and Logout Authentication System

Today, I worked on implementing the login and logout authentication system in my Django project. Below is a summary of what I accomplished:

### Key Learnings
- **Django Authentication System**:
  - Configured Django's built-in `login` and `logout` views to handle user authentication.
  - Created custom login and logout pages using Django forms and views.

- **Login Functionality**:
  - Integrated the `authenticate` and `login` methods in the login view to validate user credentials.
  - Displayed appropriate error messages for invalid login attempts using Django's messages framework.

- **Logout Functionality**:
  - Configured the `logout` view to log out users and redirect them to the homepage or a custom page.
  - Ensured user sessions were properly terminated on logout.

- **Frontend Integration**:
  - Designed login and logout pages using Bootstrap for a polished and user-friendly interface.
  - Incorporated form validation and feedback alerts to improve the user experience.

---

### Code and Files
You can find the code and exercises from today's session in this [day_2](./day_2) folder of this repository.

---

### Challenges and Insights
- Learned how to use Django's `auth` module to manage user sessions efficiently.
- Implemented robust error handling for incorrect login credentials.
- Improved the navigation experience by integrating login/logout links in the navbar.

---

### Resources
- [Django Authentication Documentation](https://docs.djangoproject.com/en/stable/topics/auth/default/)
- [Bootstrap Forms Documentation](https://getbootstrap.com/docs/5.1/forms/overview/)
- YouTube Channel: [The Ark Pro Coder](https://www.youtube.com/@ARKPROCODER)

---

Stay tuned for Day 8!

