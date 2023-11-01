from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def generate_password():
    password_input.delete(0, END)
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]
    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_data = {
        website_input.get(): {
            "email": email_input.get(),
            "password": password_input.get()
        }
    }
    f = open("data.json", "w")
    if len(website_input.get()) == 0 or len(password_input.get()) == 0:
        messagebox.showerror(title="Error", message="Website or password field is empty")
    else:
        json.dump(new_data, f, indent=4)
        messagebox.showinfo(title="New Data", message="Saved")
        website_input.delete(0, END)
        email_input.delete(0, END)
        password_input.delete(0, END)


def search():
    try:
        with open("data.json", "r") as file:
            file = json.load(file)
            key = website_input.get()
            mail = file[key]["email"]
            password = file[key]["password"]
            messagebox.showinfo(title="Info", message=f"Your email: {mail}\n Your password: {password}")

    except KeyError:
        messagebox.showinfo(title="oops", message="No such Website")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=20, pady=20, bg="white")
window.title("Password Manager")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=0, row=0, columnspan=2)

website_text = Label(text="Website: ", bg="white")
website_text.grid(column=0, row=1, padx=5, pady=5)
website_input = Entry(width=25)
website_input.grid(column=1, row=1, rowspan=2, padx=5, pady=5, sticky="nw")
website_input.focus()
generate = Button(text="Generate Password", command=generate_password)
generate.grid(column=1, row=3, padx=5, pady=5, sticky="e")
search = Button(width=12, text="Search", command=search)
search.grid(column=1, row=1, sticky="e")
email_text = Label(text="Email/Username: ", width=35, bg="white")
email_text.grid(column=0, row=2, padx=5, pady=5)
email_input = Entry(width=35)
email_input.grid(column=1, row=2, rowspan=2, padx=5, pady=5, sticky="nw")
email_input.insert(0, "example@example.com")
password = Label(text="Password: ", bg="white")
password.grid(column=0, row=3, padx=5, pady=5)
password_input = Entry(width=21)
password_input.grid(column=1, row=3, padx=5, pady=5, sticky="w")
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, rowspan=2, padx=5, pady=5)
window.mainloop()
