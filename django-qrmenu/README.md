# QRMenu - QR Code Generator for Restaurant Menus

## Description

QRMenu is a simple and efficient web application that generates QR codes for restaurant menus. With this tool, restaurant owners can easily create QR codes that link to their online menus, providing customers with a contactless way to view the menu directly on their smartphones.

## Features

- **Generate QR Codes**: Create QR codes that link to a restaurant's online menu.
- **Customizable Restaurant Name**: Input the restaurant's name to personalize the QR code.
- **Easy-to-use Form**: Simple form to input the restaurant name and menu URL.
- **Downloadable QR Code**: Once the QR code is generated, it can be downloaded as a PNG file.

## Technologies Used

- **Django**: The web framework used for backend development.
- **Python**: Programming language for server-side logic.
- **Bootstrap**: Frontend framework for responsive design.
- **qrcode**: Python library to generate QR codes.

### Steps to Install

1. **Clone the repository**:
    ```bash
    git clone https://github.com/asileayuba/100-days-of-code.git
    cd 100-days-of-code/django-qrmenu
    ```

2. **Set up a virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
   - **For Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - **For macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Migrate the database**:
    ```bash
    python manage.py migrate
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```
    The app will now be running at `http://127.0.0.1:8000`.

## Usage

- On the main page, enter the restaurant name and the URL for the online menu in the form.
- After submitting the form, a QR code will be generated that links to the provided menu URL.
- The QR code can be downloaded as a PNG file.


## Contributing

Feel free to fork this repository and submit a pull request if you have improvements or bug fixes. Contributions are welcome!

1. Fork the repository.
2. Create a new branch for your feature/bug fix.
3. Make your changes and commit them.
4. Push your changes and open a pull request.

## License

This project is licensed under the MIT License.


