import tkinter
from tkinter import messagebox
import random
import pyperclip
import json

def new_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for x in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for x in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for x in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    pyperclip.copy(password)

#-----------------------------------ADD------------------------------------------------

def add_to_file():
    website = website_entry.get()
    email = email_entry.get()
    pw = password_entry.get()
    new_data = {website: {
            "email": email,
            "password": pw
        }
    }

    if len(email) == 0 or len(pw) == 0:
        messagebox.showinfo(title="Try Again!", message="You didn't enter any information, please fill every box!")
    else:
        try:
            with open("./Day 30/data.json", "r") as data_file:
                # json.dump(new_data, data_file, indent=4)  --> needs to be in write mode 'w'  (writing)
                data = json.load(data_file)  # --> needs to be in read mode 'r'  (reading)
                    #data.update(new_data)                      # (updating)
        except FileNotFoundError:
            with open("./Day 30/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("./Day 30/data.json", 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")

#-----------------------------------------Find PW/Mail---------------------------------------------

def search_dictionary():
    email = email_entry.get()
    pw = password_entry.get()
    searched_website = website_entry.get()

    try:
        with open("./Day 30/data.json", 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="Unfortunately there is no password or email set for this website! Try again.")
    else:
       if searched_website in data:
            searched_email = data[searched_website]["email"]
            searched_pw = data[searched_website]["password"]
            messagebox.showinfo(title=f"{searched_website}", message=f"Your email: {searched_email} \nYour password: {searched_pw}")
       else:
            messagebox.showinfo(title="Oops", message="Unfortunately there is no password or email set for this website! Try again.")


#-----------------------------------UI-------------------------------------------------
window = tkinter.Tk()
window.title("Passwor Manager.")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(height=200, width=200)
photoimage = tkinter.PhotoImage(file="./Day 29/logo.png")
canvas.create_image(100, 100, image=photoimage)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text="Website: ", fg="black", padx=5, pady=5)
website_label.grid(row=1, column=0)

website_entry = tkinter.Entry(width=30)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = tkinter.Button(text="Search", command=search_dictionary, width=14)
search_button.grid(row=1, column=2)

email_label = tkinter.Label(text="Email/Username: ", fg="black", padx=5, pady=5)
email_label.grid(row=2, column=0)

email_entry = tkinter.Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "kittanjustin@gmail.com")

password_label = tkinter.Label(text="Password: ", fg="black", padx=5, pady=5)
password_label.grid(row=3, column=0)

password_entry = tkinter.Entry(width=30)
password_entry.grid(row=3, column=1)

generate_password = tkinter.Button(text="Generate Password", command=new_password)
generate_password.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=43, padx=5, pady=5, command=add_to_file)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()