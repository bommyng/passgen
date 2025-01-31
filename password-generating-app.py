import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate a random password
def generate_password():
    try:
        length = int(entry_length.get())
        if length < 4:
            raise ValueError("Password length should be at least 4.")
        
        # Define possible characters
        characters = string.ascii_letters + string.digits + string.punctuation
        
        # Generate the password
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Display the generated password
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))

# Function to copy password to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(entry_password.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("500x200")

# Create and place the widgets
label_length = tk.Label(root, text="Password Length:")
label_length.pack(pady=10)

entry_length = tk.Entry(root, width=10)
entry_length.pack(pady=5)

button_generate = tk.Button(root, text="Generate Password", command=generate_password)
button_generate.pack(pady=5)

entry_password = tk.Entry(root, width=40)
entry_password.pack(pady=5)

button_copy = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
button_copy.pack(pady=10)

# Start the main loop
root.mainloop()
