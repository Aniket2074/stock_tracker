import streamlit as st
import sqlite3

# Function to create the users table
def create_users_table():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Function to insert a new user into the database
def insert_user(name, email, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
    conn.commit()
    conn.close()

# Function to check if email already exists in the database
def is_email_unique(email):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users WHERE email=?", (email,))
    count = cursor.fetchone()[0]
    conn.close()
    return count == 0

# Function to open the login page after successful registration
def open_login_page():
    st.write('<meta http-equiv="refresh" content="0;URL=/login_page.py">', unsafe_allow_html=True)

# Function to fetch all users from the database
def fetch_all_users():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

# Function to delete a user from the database
def delete_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    conn.close()

def main():
    st.title("User Management")

    create_users_table()  # Create users table if it doesn't exist
    
    # User Registration Section
    st.header("User Registration")
    name = st.text_input("Name", key="name_input")
    email = st.text_input("Email", key="email_input")
    password = st.text_input("Password", type="password", key="password_input")
    confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password_input")
    if st.button("Register", key="register_button"):
        if password != confirm_password:
            st.error("Passwords do not match.")
        elif not is_email_unique(email):
            st.error("Email already exists. Please choose another email.")
        else:
            insert_user(name, email, password)
            st.success(f"Registration successful for {name} with email {email}.")
    
    # View registered users
    st.header("Registered Users")
    users = fetch_all_users()
    for user in users:
        st.write(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")
    
    # Delete user
    st.header("Delete User")
    selected_user_id = st.selectbox("Select User ID to delete:", [user[0] for user in users])
    if st.button("Delete User"):
        delete_user(selected_user_id)
        st.success("User deleted successfully.")

if __name__ == "__main__":
    main()
