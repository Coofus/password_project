from tkinter import *

#Saving the password

def save():

    website = website_box.get()
    email = email_box.get()
    password = password_box.get()

    with open('data.txt', 'a') as data_file:
        data_file.write(f'{website} | {email} | {password}\n')
        website_box.delete(0, END)
        password_box.delete(0, END)

#Setting up the UI#
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

canvas = Canvas(height=200, width=250, )
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)
canvas.columnconfigure(0, weight=1)
canvas.rowconfigure(0, weight=1)

#Adding Labels
website_l = Label(text="Website")
website_l.grid(row=1, column=0)

email_l = Label(text="Email/Username")
email_l.grid(row=2, column=0)

password_l = Label(text="Password")
password_l.grid(row=3, column=0)

#Entry Boxes
website_box = Entry(width=42)
website_box.grid(row=1, column=1, columnspan=2, pady=5)
website_box.focus()

email_box = Entry(width=42)
email_box.grid(row=2, column=1, columnspan=2, pady=5)
email_box.insert(0, 'chrisarr1220@hotmail.com')

password_box = Entry(width=42)
password_box.grid(row=3, column=1, columnspan=2, pady=5)

#Buttons
generate_password = Button(text="Generate Password")
generate_password.grid(row=3, column=3)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()