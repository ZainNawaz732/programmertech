import tkinter as tk
from tkinter import messagebox
import random
import string


# Function to generate the password
def generate_password():
    try:
        length = int(entry_length.get())

        if length <= 0:
            raise ValueError("Password length must be a positive integer.")

        characters = string.ascii_letters + string.digits 
        password = ''.join(random.choice(characters) for i in range(length))

        entry_password.config(state=tk.NORMAL)
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
        entry_password.config(state=tk.DISABLED)

    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))


# Function to register the user
def register_user():
    username = entry_username.get()
    password = entry_password.get()

    if username and password:
        messagebox.showinfo("Registration Successful", f"User '{username}' registered with password: {password}")
    else:
        messagebox.showerror("Registration Failed", "Please fill in all fields")


# Main application window setup
root = tk.Tk()
root.title("User Registration with Password Generator")
root.geometry("400x300")

# Username
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=5)

entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Password length
label_length = tk.Label(root, text="Password Length:")
label_length.pack(pady=5)

entry_length = tk.Entry(root)
entry_length.pack(pady=5)

# Generate Password Button
button_generate = tk.Button(root, text="Generate Password", command=generate_password)
button_generate.pack(pady=10)

# Password Entry
label_password = tk.Label(root, text="Generated Password:")
label_password.pack(pady=5)

entry_password = tk.Entry(root, state=tk.DISABLED)
entry_password.pack(pady=5)

# Register Button
button_register = tk.Button(root, text="Register", command=register_user)
button_register.pack(pady=10)

# Run the application
root.mainloop()
