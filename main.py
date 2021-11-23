from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT = "Arial", 12, "normal"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pswd():
    web = website_input.get()
    pswd = psswrd_input.get()
    mail = mail_input.get()
    print(web)
    print(pswd)
    with open("data.txt", "w") as file:
        file.write(f"{web} | {mail} | {pswd} ")


# ---------------------------- UI SETUP ------------------------------- #
# create the window
window = Tk()
window.title(" Password Manager ")
window.config(padx=50, pady=50)

# create the canvas to insert the logo
canvas = Canvas(width=200, height=200)

logo_pass = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_pass)
canvas.grid(row=0, column=1)

# adding widget : LABEl and entry
label_website = Label(text="Website:")
label_website.grid(row=1, column=0)

label_mail = Label(text="Email/Username:")
label_mail.grid(row=2, column=0)

label_psswrd = Label(text="Password:")
label_psswrd.grid(row=3, column=0)

# Entries :
psswrd_input = Entry(width=35)
psswrd_input.grid(row=3, column=1, columnspan=2)

mail_input = Entry(width=35)
mail_input.insert(0, "dummy@email.com")
mail_input.grid(row=2, column=1, columnspan=2)

website_input = Entry(width=35)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)

# btn
btn_psswrd = Button(text="Generate Password")
btn_psswrd.grid(row=3, column=2)

btn_add = Button(text="Add", width=36, command=save_pswd)
btn_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
