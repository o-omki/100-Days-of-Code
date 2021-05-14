import tkinter
from tkinter import messagebox
from string import ascii_letters, digits
import random
import json

symbols = "!#$%&()*+"

def search_password():
    try:
        with open(r"days\21-30\day30\password_manager\passwords.json", "r") as file:
            data = json.load(file)            
    except FileNotFoundError:
        messagebox.showerror(title = "No Record Found", message = "You haven't saved any passwords yet!")    
    else:
        website = website_input.get().strip()
        if website in data:
            details = data[website]
            messagebox.showinfo(title = website.title(), message = f"Email/Username: {details['email']} \nPassword: {details['password']}")
        else:
            messagebox.showinfo(title = website.title(), message = "No password for this website exists.")        
                    

def generate_password():
    password_generated = []

    random_letters = [random.choice(ascii_letters) for _ in range(random.randint(8, 10))]
    random_numbers = [random.choice(digits) for _ in range(random.randint(2, 4))]
    random_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_generated = random_letters + random_numbers + random_symbols
    random.shuffle(password_generated)
    password = "".join(password_generated)
    password_input.insert(0, password)

def save_password():
    website = website_input.get().strip()
    email = email_input.get()
    password = password_input.get().strip()
    new_data = {
        website:
        {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title = "Oops", message = "Please make sure you haven't left any fields empty.")
  
    else:
        is_ok = messagebox.askokcancel(title = website, message = f"The details entered: \nEmail: {email} \nPassword: {password} \nDo you want to save?")
        if is_ok:
            try:
                with open(r"days\21-30\day30\password_manager\passwords.json", "r") as file:
                    data = json.load(file)

            except FileNotFoundError:
                with open(r"days\21-30\day30\password_manager\passwords.json", "w") as file:
                    json.dump(new_data, file, indent = 4)

            else:
                data.update(new_data)
                with open(r"days\21-30\day30\password_manager\passwords.json", "w") as file:
                    json.dump(data, file, indent = 4)

            finally:
                website_input.delete(0, tkinter.END)
                password_input.delete(0, tkinter.END)

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

canvas = tkinter.Canvas(height = 200, width = 200)
lock_image = tkinter.PhotoImage(file = r"days\21-30\day29\password_manager\data\logo.png")
canvas.create_image(100, 100, image = lock_image)
canvas.grid(row = 0, column = 1)

website_label = tkinter.Label(text = "Website:")
website_label.grid(row = 1, column = 0) 
email_label = tkinter.Label(text = "Email/Username:")
email_label.grid(row = 2, column = 0)
password_label = tkinter.Label(text = "Password:")
password_label.grid(row = 3, column = 0)

website_input = tkinter.Entry(width = 21)
website_input.grid(row = 1, column = 1)
website_input.focus()
email_input = tkinter.Entry(width = 39)
email_input.grid(row = 2, column = 1, columnspan = 2)
email_input.insert(0, "abc@gmail.com")
password_input = tkinter.Entry(width = 21)
password_input.grid(row = 3, column = 1)

generate_button = tkinter.Button(text = "Generate Password", command = generate_password)
generate_button.grid(row = 3, column = 2)
add_button = tkinter.Button(text = "Add", width = 33, command = save_password)
add_button.grid(row = 4, column = 1, columnspan = 2)
search_button = tkinter.Button(text = "Search:", width = 13, command = search_password)
search_button.grid(row = 1, column = 2)


window.mainloop() 