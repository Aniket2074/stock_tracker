import streamlit as st
import sqlite3

# Function to fetch user from the database based on email
def fetch_user(email):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email=?", (email,))
    user = cursor.fetchone()
    conn.close()
    return user

def main():
    st.title("Login Page")
    
    # Get user inputs
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    # Login button
    if st.button("Login"):
        user = fetch_user(email)
        if user is None:
            st.error("User not found. Please register.")
        elif user[3] != password:
            st.error("Incorrect password. Please try again.")
        else:
            st.experimental_set_query_params(logged_in=True)  # Set query parameter upon successful login
            st.success(f"Logged in successfully as {user[1]} with email {user[2]}.")

if __name__ == "__main__":
    main()
