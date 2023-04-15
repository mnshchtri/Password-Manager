import tkinter as tk
from tkinter import messagebox
import mysql.connector
import string
import random


def generate_password():
    # Define the character set to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password of length 12
    password = ''.join(random.choice(characters) for i in range(12))
    # Update the password entry field with the generated password
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def save_password():
    # Get the values from the entry fields
    service = service_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    # Connect to the MySQL database
    db = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="password_manager"
    )
    cursor = db.cursor()
    # Insert the values into the passwords table
    sql = "INSERT INTO passwords (service, username, password) VALUES (%s, %s, %s)"
    values = (service, username, password)
    cursor.execute(sql, values)
    db.commit()
    # Display a success message
    messagebox.showinfo("Success", "Password saved successfully!")


# Create the main window
window = tk.Tk()
window.title("Password Manager")

# Create the labels and entry fields for the service, username, and password
service_label = tk.Label(window, text="Service:")
service_label.grid(row=0, column=0, padx=5, pady=5)
service_entry = tk.Entry(window)
service_entry.grid(row=0, column=1, padx=5, pady=5)

username_label = tk.Label(window, text="Username:")
username_label.grid(row=1, column=0, padx=5, pady=5)
username_entry = tk.Entry(window)
username_entry.grid(row=1, column=1, padx=5, pady=5)

password_label = tk.Label(window, text="Password:")
password_label.grid(row=2, column=0, padx=5, pady=5)
password_entry = tk.Entry(window)
password_entry.grid(row=2, column=1, padx=5, pady=5)

# Create the buttons for generating a password and saving the password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=2, padx=5, pady=5)

save_button = tk.Button(window, text="Save Password", command=save_password)
save_button.grid(row=3, column=1, padx=5, pady=5)

# Start the main loop
window.mainloop()

