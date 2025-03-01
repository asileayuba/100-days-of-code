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


# 100 Days of Code: Day 8

## Django Login with Google Account Integration

Today, I focused on integrating Google account login functionality into my Django project. Below is a summary of what I accomplished:

### Key Learnings
- **Google OAuth2 Integration**:
  - Installed and configured the `social-auth-app-django` package to enable OAuth2 authentication with Google.
  - Set up a Google Developer project to obtain the necessary credentials (client ID and client secret) for OAuth2 integration.

- **Configured Settings**:
  - Added the Google authentication backend to Django's `AUTHENTICATION_BACKENDS` in the settings file.
  - Configured required Google API settings, including client ID, secret, and redirect URL.

- **Redirect URL Handling**:
  - Ensured users are redirected to the appropriate page after successful authentication via Google, handling first-time user creation if necessary.

- **Frontend Integration**:
  - Created a login button that redirects users to the Google authentication flow.
  - Customized the button styling to align with the design of the website.

---

### Code and Files
You can find the code and exercises from today's session in this [day_2](./day_2) folder of this repository.

---

### Challenges and Insights
- The integration of Google login required handling multiple steps, including setting up the API credentials and configuring Django settings.
- OAuth2 flow provided a seamless login experience, but required ensuring security around user data.

---

### Resources
- [Django Social Auth Documentation](https://python-social-auth.readthedocs.io/en/latest/)
- [Google OAuth2 Documentation](https://developers.google.com/identity/protocols/oauth2)
- YouTube Channel: [The Ark Pro Coder](https://www.youtube.com/@ARKPROCODER)

---

Stay tuned for Day 9!


# 100 Days of Code: Day 9

## Django Login with Google Account (Continued)

Today, I continued to work on the Google account login integration in my Django project, refining and troubleshooting the setup. Below is a summary of what I accomplished:

### Key Learnings
- **Google Authentication Flow**:
  - Ensured the correct handling of user sessions upon successful authentication via Google.
  - Implemented profile creation for users who sign in with Google for the first time.

- **Error Handling**:
  - Managed errors that could arise during the authentication process, such as incorrect or missing credentials.
  - Displayed appropriate messages to users in case of failure to authenticate.

- **User Experience Enhancement**:
  - Refined the UI for the Google login button, improving visibility and interaction.
  - Implemented an easy logout process for users signed in via Google, ensuring a seamless transition.

---

### Code and Files
You can find the code and exercises from today's session in this [day_2](./day_2) folder of this repository.

---

### Challenges and Insights
- Integrating third-party authentication with Django required understanding how OAuth2 works and handling edge cases related to user data retrieval.
- Learning how to debug and troubleshoot common errors in OAuth2 flow helped enhance my debugging skills.

---

### Resources
- [Django Social Auth Documentation](https://python-social-auth.readthedocs.io/en/latest/)
- [Google OAuth2 Documentation](https://developers.google.com/identity/protocols/oauth2)
- YouTube Channel: [The Ark Pro Coder](https://www.youtube.com/@ARKPROCODER)

---

Stay tuned for Day 10!


```markdown
# 100 Days of Code: Day 10

## Google and Facebook Account Login Integration

Today, I focused on consolidating my understanding of third-party login integrations by revisiting the **django-allauth** documentation and enhancing my project. Below is a summary of what I accomplished:

### Key Learnings
- **Refining Google Login Integration**:
  - Explored the **django-allauth** documentation in-depth to better understand its features and configurations.
  - Made corrections to the initial implementation and ensured a seamless authentication flow.

- **Added Facebook Account Login Integration**:
  - Configured Facebook login alongside Google login using **django-allauth**.
  - Set up Facebook App credentials (App ID and App Secret) and configured them in the Django project.
  - Implemented a user-friendly frontend login option for Facebook authentication.

- **Multi-Provider Support**:
  - Ensured that users could log in using either Google or Facebook without conflicts.
  - Improved the authentication backend handling to support multiple providers.

---

### Code and Files
You can find the code and exercises from today's session in this [day_2](./day_2) folder of this repository.

---

### Challenges and Insights
- Revisiting the **django-allauth** documentation helped me understand how to optimize configurations for real-world applications.
- Adding multiple authentication providers required careful attention to settings and flow, but it significantly improved the project's usability.

---

### Resources
- [django-allauth Documentation](https://django-allauth.readthedocs.io/en/latest/)
- [Google OAuth2 Documentation](https://developers.google.com/identity/protocols/oauth2)
- [Facebook Login Documentation](https://developers.facebook.com/docs/facebook-login/)

---

### Next Steps
This wraps up my work with **django-allauth**, and I am excited to move forward with exploring Django models in the coming days!

Stay tuned for Day 11! 🚀
```


# 100 Days of Code: Day 11

## Django Models, Contact Page, and Data Management

Today, I explored Django models and worked on implementing a **Contact Page** that stores user-submitted data in the Django admin panel. Below is a summary of what I accomplished:

### Key Learnings
- **Django Models**:
  - Learned how to define and create Django models for database interaction.
  - Explored model fields, their types, and their purpose (e.g., `CharField`, `EmailField`, `TextField`, etc.).
  - Ran migrations to apply changes to the database.

- **Creating a Contact Page**:
  - Designed a contact form with fields for `Name`, `Email`, `Subject`, and `Message`.
  - Set up a view to handle form submissions and render success messages.
  - Styled the contact page using Bootstrap to improve user experience.

- **Storing Data in the Admin Panel**:
  - Registered the Contact model in `admin.py` to manage submissions through the Django admin interface.
  - Tested data persistence by submitting forms and verifying entries in the admin panel.

---

### Code and Files
You can find the code and exercises from today's session in this [day_2](./day_2) folder of this repository.

---

### Challenges and Insights
- Defining and working with Django models clarified how Django ORM simplifies database management.
- Integrating form submissions with the database was a valuable exercise in connecting frontend and backend workflows.

---

### Resources
- [Django Documentation on Models](https://docs.djangoproject.com/en/stable/topics/db/models/)
- [Bootstrap Documentation](https://getbootstrap.com/)
- YouTube Channel: [The Ark Pro Coder](https://www.youtube.com/@ARKPROCODER)

---

Stay tuned for Day 12! 🚀


# 100 Days of Code: Day 12 and 13

## Sending Emails Dynamically in Django

Today, I implemented functionality to send emails dynamically using Django. This was a rewarding experience as I delved deeper into Django's email capabilities. Here's a summary of what I accomplished:

### Key Learnings
- **Email Backend Configuration**:
  - Configured Django's email backend in the `settings.py` file.
  - Set up SMTP settings for sending emails using Gmail (e.g., `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, and `EMAIL_USE_TLS`).

- **Sending Emails Dynamically**:
  - Created a function in the views to handle sending emails.
  - Used Django's `send_mail` function to send emails with dynamic content.
  - Set up email templates to customize the email body dynamically based on user input from the contact form.

- **Testing the Email Functionality**:
  - Submitted test data from the contact form and verified the email delivery.
  - Encountered and resolved issues with Gmail's security settings, ensuring smooth email delivery.

---

### Code and Files
You can find the code and exercises from today's session in this [day_2](./day_2) folder of this repository.

---

### Challenges and Insights
- Configuring Gmail SMTP required enabling "Allow less secure apps" and app-specific passwords for secure access.
- Sending emails programmatically provided valuable insights into Django's capabilities for real-world applications.

---

### Resources
- [Django Documentation: Sending Emails](https://docs.djangoproject.com/en/stable/topics/email/)
- [Google SMTP Configuration Guide](https://support.google.com/mail/answer/7126229?hl=en)
- YouTube Channel: [The Ark Pro Coder](https://www.youtube.com/@ARKPROCODER)

---

Stay tuned for Day 14! 🚀📧


# 100 Days of Code: Day 14

## Creating a Django Blog Page and Displaying Blog Content Dynamically

Today's focus was on building a dynamic blog page using Django. This involved creating models, views, and templates to display blog content seamlessly. Here's what I accomplished:

### Key Learnings
- **Creating the Blog Model**:
  - Defined a `Blog` model with fields such as `title`, `author`, `description`, `img`, and `TimeStamp`.
  - Used Django's ORM to design and interact with the database.

- **Database Migrations**:
  - Generated and applied migrations to create the `Blog` table in the database.

- **Fetching and Displaying Blog Content**:
  - Created a view to query and fetch blog posts from the database.
  - Passed the fetched content to the template for rendering.

- **Dynamic Blog Page**:
  - Designed a responsive blog page template using Bootstrap for styling.
  - Integrated Django's template language to loop through blog posts and display them dynamically.

- **URL Routing**:
  - Configured URLs to map the blog view to the blog page.
  - Ensured proper navigation between the blog page and other sections of the website.

---

### Code and Files
You can find the code and related files for today's work in the [day_2](./day_2) folder of this repository.

---

### Challenges and Insights
- Learned the importance of structuring models to reflect real-world data effectively.
- Debugged issues with model migrations and gained a better understanding of Django's migration system.
- Using Bootstrap ensured the blog page is both functional and visually appealing.

---

### Resources
- [Django Documentation: Models](https://docs.djangoproject.com/en/stable/topics/db/models/)
- [Bootstrap Documentation](https://getbootstrap.com/)
- YouTube Channel: [The Ark Pro Coder](https://www.youtube.com/@ARKPROCODER)

---


Stay tuned for Day 15! 🚀📝


# 100 Days of Code: Day 15

## Implementing Django Search Functionality in My Project

Today's focus was on adding a search feature to my Django project, allowing users to search for specific content dynamically. Here's a summary of what I accomplished:

### Key Learnings
- **Setting Up the Search Form**:
  - Created an HTML form with a search input field.
  - Added a `GET` method to handle search queries submitted by the user.

- **Handling Search Queries in Views**:
  - Used Django's ORM to filter database records based on the user's search input.
  - Implemented case-insensitive search for better user experience.

- **Displaying Search Results**:
  - Created a dedicated template to display the filtered results.
  - Used Django's template language to handle dynamic content rendering.

- **URL Routing**:
  - Configured a URL pattern to connect the search view to the appropriate endpoint.

---

### Code and Files
You can find the code and related files for today's work in the [day_2](./day_2) folder of this repository.

---

### Challenges and Insights
- Handling empty search queries required adding validation logic in the view.
- Optimizing the search query for performance was crucial to ensure quick response times.


---

### Resources
- [Django Documentation: QuerySet API](https://docs.djangoproject.com/en/stable/ref/models/querysets/)


---

Stay tuned for Day 16! 


# 100 Days of Code: Day 16

## Customizing the Django Home Page

Today's focus was on customizing the Django home page to create a more engaging and user-friendly landing experience. Here's what I accomplished:

### Key Learnings
- **Customizing the Default Home Page**:
  - Replaced the default Django welcome page with a fully customized HTML page.
  - Integrated Bootstrap for styling and responsiveness.

- **Dynamic Content Rendering**:
  - Passed dynamic data from the view to the template to display content like recent posts, user-specific greetings, and featured sections.
  - Used Django's template tags to handle conditional content rendering.

- **Enhanced Navigation**:
  - Added a navigation bar with links to key sections like Blog, Contact, and Login/Signup pages.
  - Implemented responsive navigation for mobile and tablet users.

- **Footer Design**:
  - Designed a footer with social media links, copyright information, and quick navigation.

---

### Code and Files
You can find the updated home page template and associated files in the [day_2](./day_2) folder of this repository.

---

### Challenges and Insights
- Creating a dynamic home page required thoughtful structuring of templates and views.
- Ensuring cross-browser compatibility and responsiveness involved extensive testing and tweaking.
- Passing meaningful dynamic data to the home page improved user engagement.

---

### Resources
- [Django Template Documentation](https://docs.djangoproject.com/en/stable/ref/templates/)
- [Bootstrap Components](https://getbootstrap.com/docs/5.0/components/)

---


Stay tuned for Day 17! 

# 100 Days of Code: Day 17

## Debugging the Django Project

Today, I wrapped up my foundational learning of Django by focusing on debugging the project I’ve been working on. Here’s a summary of what I accomplished:

### Key Learnings
- **Debugging and Error Handling**:
  - Identified and resolved errors in views, templates, and static file configurations.
  - Used Django's built-in debug tools to track issues efficiently.
  - Refined the project structure to improve maintainability.

- **Project Recap**:
  - Learned to create a Django project and app.
  - Explored core components such as models, views, templates, and the settings file.
  - Integrated Bootstrap for responsive and aesthetic designs.
  - Implemented user authentication features, including login, logout, and third-party account logins (Google and Facebook) using `django-allauth`.
  - Developed a contact page with dynamic data storage and email-sending functionality.
  - Added search functionality to enhance user navigation.
  - Customized the home page to dynamically render content and improve user experience.
  - Built a blog page that displays blog content dynamically.

---

### Challenges and Insights
- Debugging reinforced the importance of understanding error messages and logs.
- This project helped me solidify my knowledge of Django basics and apply problem-solving skills to real-world scenarios.

---

### Next Steps
With the foundational concepts of Django well understood, I’m excited to move forward and work on a more standard and complex project. This will:
- Help me deepen my understanding of Django.
- Enhance my problem-solving skills by tackling more advanced challenges.
- Provide opportunities to build features that simulate real-world applications.

---

### Final Note on Django Basics
This journey of learning Django basics has been incredibly rewarding. From setting up projects to creating dynamic and responsive web pages, I’ve gained invaluable insights into web development with Django. 

Stay tuned as I take on my next challenge—a more advanced Django project to further grow as a developer. 🚀💻
