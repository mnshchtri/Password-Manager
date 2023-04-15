import tkinter as tk
import mysql.connector
import secrets

# Define the MySQL connection parameters
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="password_manager"
)

# Define a function to generate a random password
def generate_password():
    chars_1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=[]{};:,./<>?`~'
    chars_2 = '0123456789'
    password = ''.join(secrets.choice(chars_1 + chars_2) for i in range(30))
    return password

# Define a function to save the password to the MySQL database
def save_password():
    service = service_entry.get()
    username = username_entry.get()
    password = generate_password()
    cursor = mydb.cursor()
    sql = "INSERT INTO passwords (service, username, password) VALUES (%s, %s, %s)"
    val = (service, username, password)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()
    service_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_label.config(text=password)
    status_label.config(text="Password saved!")

# Create the Tkinter GUI
root = tk.Tk()
root.title("Password Manager")

service_label = tk.Label(root, text="Service:")
service_label.pack()
service_entry = tk.Entry(root)
service_entry.pack()

username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_button = tk.Button(root, text="Generate Password", command=generate_password)
password_button.pack()

save_button = tk.Button(root, text="Save Password", command=save_password)
save_button.pack()

password_label = tk.Label(root, text="")
password_label.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
