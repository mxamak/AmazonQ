import tkinter as tk
from tkinter import messagebox

# Create the main application window (hidden)
root = tk.Tk()
root.withdraw()  # Hide the root window

# Show the message box with "Hello, world!"
messagebox.showinfo("Greeting", "This script has been downloaded from Github and executed. It can be found in your downloads folder.")
