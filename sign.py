import tkinter as tk
from tkinter import messagebox

# Function to handle the sign-in button click
def sign_in():
    username = entry_username.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()

    if username and password and confirm_password:
        if password == confirm_password:
            # Save the input data to a file
            with open("sign_in_data.txt", "a") as file:
                file.write(f"Username: {username}\n")
                file.write(f"Password: {password}\n\n")
                file.write(f"Confirm Password: {confirm_password}\n")
            
            # Show success message
            messagebox.showinfo("Sign In", "Sign In Successful!")
        else:
            messagebox.showerror("Error", "Passwords do not match.")
    else:
        # Show error message
        messagebox.showerror("Error", "Please enter username and both passwords.")

# Function to change the style on hover
def on_enter(event):
    event.widget.config(bg='lightblue')

def on_leave(event):
    event.widget.config(bg='SystemButtonFace')

def on_label_enter(event):
    event.widget.config(fg='blue')

def on_label_leave(event):
    event.widget.config(fg='black')

# Create the main window
window = tk.Tk()
window.title("Sign In")
window.geometry("400x400")

# Create and place the username label and entry
label_username = tk.Label(window, text="Username:")
label_username.pack(pady=5)
label_username.bind("<Enter>", on_label_enter)
label_username.bind("<Leave>", on_label_leave)

entry_username = tk.Entry(window, width=30)
entry_username.pack(pady=5)

# Create and place the password label and entry
label_password = tk.Label(window, text="Password:")
label_password.pack(pady=5)
label_password.bind("<Enter>", on_label_enter)
label_password.bind("<Leave>", on_label_leave)

entry_password = tk.Entry(window, width=30, show="*")
entry_password.pack(pady=5)

# Create and place the confirm password label and entry
label_confirm_password = tk.Label(window, text="Confirm Password:")
label_confirm_password.pack(pady=5)
label_confirm_password.bind("<Enter>", on_label_enter)
label_confirm_password.bind("<Leave>", on_label_leave)

entry_confirm_password = tk.Entry(window, width=30, show="*")
entry_confirm_password.pack(pady=5)

# Create and place the sign-in button
button_sign_in = tk.Button(window, text="Sign In", command=sign_in)
button_sign_in.pack(pady=20)
button_sign_in.bind("<Enter>", on_enter)
button_sign_in.bind("<Leave>", on_leave)

# Run the application
window.mainloop()
