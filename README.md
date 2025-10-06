# User Management System with Streamlit and MySQL

A secure and interactive web application built with Python, Streamlit, and MySQL database to manage user registration, login, and account management functionalities.

## Features
- **User Registration** with strong password policies:
  - Minimum 8 characters
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one digit
  - At least one special character
- **User Login** with username and password authentication
- **Account Management:**
  - Change username
  - Change password (with validation)
  - Delete user account
- Database-driven persistence using MySQL
- Clean and simple user interface powered by Streamlit

## Installation

1. Clone the repository:
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

2. Install the required packages:
pip install streamlit mysql-connector-python


3. Setup MySQL database:
- Create a database named `week4`
- Update the database connection credentials in the script if needed

## Usage

Run the Streamlit app:
streamlit run app.py


- Use the sidebar to switch between **Login** and **Register**.
- After logging in, access the welcome page to manage your account.

## Screenshots

![Change Password](/images/ChangePassword.png)  
![Change Username](/images/ChangeUsername.png)  
![Delete User](/images/DeleteUser.png)  
![Login Page](/images/LoginPage.png)  
![Registration Page](/images/RegistrationPage.png)  

## Security Notes

- Passwords are stored as plain text currently. For production, I will implement proper hashing (e.g., bcrypt).
- Input validation is implemented to enforce password strength and username uniqueness.

## Future Improvements

- Password hashing and salting
- Email verification on registration
- Enhanced frontend design
- Deployment to cloud platforms like Streamlit Cloud or Heroku



