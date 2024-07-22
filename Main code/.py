import tkinter as tk
from tkinter import Entry, Button, Label

def sign_up():
    pass

root = tk.Tk()
root.geometry("700x550")
email = tk.StringVar()

password = tk.StringVar()
signup_window = tk.Tk()
root.title('Sign In')

# Function to switch to the sign-up screen
def switch_to_signup():
    email.get()
    root.withdraw()  # Hide the login window
    signup_window.deiconify()  # Show the signup window
    

signin = tk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)
Button(root, text='Login', bg='#FFFDD0', font=('arial',12, 'normal'))
label = Label(root, text='sign up', bg='#F0F8FF', font=('arial', 12, 'normal'))
label.place(x=10, y=10)


root.mainloop()