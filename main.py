from tkinter import *
from tkinter import messagebox
import random
import pyperclip

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT = "Arial", 12, "normal"


def append_new_line(file_name, text_to_append):
    """Append given text as a new line at the end of file"""
    # Open the file in append & read mode ('a+')
    with open(file_name, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(text_to_append)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)  # password will contain 8 to 10 letters
    nr_symbols = random.randint(2, 4)  # will contain 2 to 4 symbols
    nr_numbers = random.randint(2, 4)  # will contain 2 to 4 numbers

    password_ltr = [random.choice(letters) for _ in range(nr_letters)]
    password_sym = [random.choice(numbers) for _ in range(nr_numbers)]
    password_num = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_num + password_sym + password_ltr
    random.shuffle(password_list)

    password = "".join(password_list)

    if psswrd_input.get != 0:
        psswrd_input.delete(0, END)
    psswrd_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pswd():
    web = website_input.get()
    mail = mail_input.get()
    pswd = psswrd_input.get()
    info_pswd = f"{web} | {mail} | {pswd} "

    if web != "" and pswd != "" and mail != "":
        is_ok = messagebox.askokcancel(title='confirmation', message="you entered : " + info_pswd + "are you sure ?")

        if is_ok:
            append_new_line("data.txt", info_pswd)
            # or file.write(info_pswd + "\n")
            messagebox.showinfo("confirmation ", "password added")
            website_input.delete(0, END)
            psswrd_input.delete(0, END)
    else:
        messagebox.showerror("error test", "Pliz dont leave any fields empty")
        print(" show msg box with error")


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
btn_psswrd = Button(text="Generate Password", command=generate_password)
btn_psswrd.grid(row=3, column=2)

btn_add = Button(text="Add", width=36, command=save_pswd)
btn_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
