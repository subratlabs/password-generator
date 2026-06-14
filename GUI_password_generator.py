import tkinter as tk
from tkinter import messagebox
import string
import secrets

def generate_password():
    try:
        lenght = int(length_entry.get())

        if lenght <= 0:
            messagebox.showerror("Error", "Enter a valid length")
            return
        charaters = (string.ascii_letters + string.digits + string.punctuation)

        password = ''.join(secrets.choice(charaters) for _ in range(lenght))

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Enter", "Please enter a number")

def copy_password():
    password = password_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")

tk.Label(root, text="Password Length:", font=("Arial", 12)).pack(pady=10)

length_entry = tk.Entry(root, font=("Arial", 12))
length_entry.pack()

tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12)).pack(pady=10)

password_entry = tk.Entry(root, font=("Arial", 12), width=30)
password_entry.pack(pady=10)


tk.Button(root, text="Copy Password", command=copy_password, font=("Arial", 12)).pack(pady=10)

root.mainloop()