from tkinter import *
from tkinter import messagebox
import password
import pyperclip

window = Tk()
window.title("Password Manager")
window.minsize(500,300)
window.config(padx=50, pady=50)


# GENERATE PASSWORD
def generate_password():
    new_pass = password.generate_pass()
    password_entry.insert(0, new_pass)
    pyperclip.copy(new_pass)


#SAVE PASSWORD
def save():

    website = website_entry.get()
    user_email = email_entry.get()
    user_password = password_entry.get()

    if len(website) + len(user_password) + len(user_email) == 0:
        messagebox.showerror("Invalid Input", "Please fill in all fields.")
    elif len(website) == 0:
        messagebox.showerror("Invalid Input", "Please fill in the Website field.")
        website_entry.focus()
    elif len(user_email) == 0:
        messagebox.showerror("Invalid Input", "Please fill in the Email field.")
        email_entry.focus()
    elif len(user_password) == 0:
        messagebox.showerror("Invalid Input", "Please fill in the Password field.")
        password_entry.focus()
    else:
        # PopUp Box
        is_ok = messagebox.askyesno("Save Password", "Are you sure you want to save this information?")

        if is_ok:

            with open("data.txt", "a") as data:
                data.write(f"{website} | {user_email} | {user_password} \n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# UI Setup

#CANVAS
canvas = Canvas(width=200,height=200)
password_logo = PhotoImage(file="logo.png")
canvas.create_image(80,100, image=password_logo)
canvas.grid(column=1,row=0)

#LABELS

#website
website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

#email/username
email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)

#password
password_label = Label(text="Password:")
password_label.grid(column=0,row=3)


#ENTRIES

#website name
website_entry = Entry(width=40)
#place curser here o launch
website_entry.focus()
website_entry.grid(column=1,row=1, sticky="ew")

#email
email_entry = Entry()
email_entry.insert(0, "test@gmail.com")
email_entry.grid(column=1,row=2, sticky="ew")

#password
password_entry = Entry(width=18)
password_entry.grid(column=1,row=3, sticky="ew")


#BUTTONS

# search button
search_button = Button(text="Search", width=15)
search_button.grid(column=1, row=1, sticky="e")

# generate button
generate_button = Button(text="Generate Password",width=15)
generate_button.grid(column=1,row=3, sticky="e")
generate_button.config(command=generate_password)

#add_Button
add_button = Button(text="Add")
add_button.grid(column=1,row=4, sticky="ew")
add_button.config(command=save)



#generate password

window.mainloop()