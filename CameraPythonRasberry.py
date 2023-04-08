#!/bin/python3

import tkinter
import customtkinter

# main window init
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("800x600")

# button functions
def button_image_function():
    print("button image pressed")

def button_record_function():
    print("button record pressed")

def button_init_function():
    print("button init pressed")

# UI
# placement variables
rely_rows = [0.03, 0.5, 0.75]
relx_columns = [0.25, 0.5, 0.75]

# first row
button_record = customtkinter.CTkButton(master=app, text="Record video", command=button_record_function)
button_record.place(relx=relx_columns[0], rely=rely_rows[0], anchor=tkinter.CENTER)

button_image = customtkinter.CTkButton(master=app, text="Capture image", command=button_image_function)
button_image.place(relx=relx_columns[1], rely=rely_rows[0], anchor=tkinter.CENTER)

button_init = customtkinter.CTkButton(master=app, text="Initialize camera", command=button_init_function)
button_init.place(relx=relx_columns[2], rely=rely_rows[0], anchor=tkinter.CENTER)

# second row
button_record = customtkinter.CTkButton(master=app, text="Record video", command=button_record_function)
button_record.place(relx=relx_columns[0], rely=rely_rows[0], anchor=tkinter.CENTER)

button_image = customtkinter.CTkButton(master=app, text="Capture image", command=button_image_function)
button_image.place(relx=relx_columns[1], rely=rely_rows[0], anchor=tkinter.CENTER)

button_init = customtkinter.CTkButton(master=app, text="Initialize camera", command=button_init_function)
button_init.place(relx=relx_columns[2], rely=rely_rows[0], anchor=tkinter.CENTER)

# first row
button_record = customtkinter.CTkButton(master=app, text="Record video", command=button_record_function)
button_record.place(relx=relx_columns[0], rely=rely_rows[0], anchor=tkinter.CENTER)

button_image = customtkinter.CTkButton(master=app, text="Capture image", command=button_image_function)
button_image.place(relx=relx_columns[1], rely=rely_rows[0], anchor=tkinter.CENTER)

button_init = customtkinter.CTkButton(master=app, text="Initialize camera", command=button_init_function)
button_init.place(relx=relx_columns[2], rely=rely_rows[0], anchor=tkinter.CENTER)

app.mainloop()

