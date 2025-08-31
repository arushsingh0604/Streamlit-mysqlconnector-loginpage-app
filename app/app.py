import streamlit as st
import mysql.connector



db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='1111',
    database='week4'
)
mycursor = db.cursor(buffered=True)

mycursor.execute("""
    CREATE TABLE IF NOT EXISTS people (
        id INT PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL
    )
""")
db.commit()

choice = st.sidebar.selectbox('Choose your option',["Login","Register"])

if choice=='Register':
    st.title("Register User")
    user = st.text_input("Enter your username:")
    passw = st.text_input("Enter your password",type='password')
    retyped_pass = st.text_input("Re-Enter your password",type='password')
    register_button = st.button("Register")
    if register_button:
        if len(user) < 5:
            st.error('Username must have a minimum of 5 characters')
        elif any(not field.strip() for field in [user, passw]):
            st.error("Please fill all the fields")
        else:
            mycursor.execute('SELECT username FROM people WHERE username=%s', (user,))
            existing_user = mycursor.fetchone()

            if existing_user:
                st.error("User already exists")
            else:
                ch = "!@#$%^&*(),.?\":<>"
                if len(passw) < 8:
                    st.error("Password must be at least 8 characters long.")
                elif not any(c.isupper() for c in passw):
                    st.error("Password must include an uppercase letter.")
                elif not any(c.islower() for c in passw):
                    st.error("Password must include a lowercase letter.")
                elif not any(c.isdigit() for c in passw):
                    st.error("Password must include a digit.")
                elif not any(c in ch for c in passw):
                    st.error("Password must include a special character.")
                elif passw != retyped_pass:
                    st.error("Your retyped password doesn't match your password")
                else:
                    mycursor.execute("INSERT INTO people (username, password) VALUES (%s, %s)", (user, passw))
                    db.commit()
                    st.success("User registered successfully")

if choice == 'Login':
    st.title('Login')
    user = st.text_input('Enter your username')
    passw = st.text_input("Enter your password", type='password')
    login_button = st.button('Login')

    if login_button:
        mycursor.execute('SELECT * FROM people WHERE username=%s', (user,))
        exist = mycursor.fetchone()

        if exist:
            if exist[1] == user and exist[2] == passw:
                st.success('Logged in successfully')
                st.switch_page(r'pages/welcome.py')
            else:
                st.error('Invalid Password')
        else:
            st.error('Username does not exist')








