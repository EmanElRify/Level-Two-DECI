# gui_example.py

import tkinter as tk

def greet():
    name = name_entry.get()
    greeting_label.config(text="Hello, " + name + "!")

# Create the main window
root = tk.Tk()
root.title("Greeting App")

# Create GUI elements
name_label = tk.Label(root, text="Enter your name:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

greet_button = tk.Button(root, text="Greet", command=greet)
greet_button.pack()

greeting_label = tk.Label(root, text="")
greeting_label.pack()

# Run the application
root.mainloop()
