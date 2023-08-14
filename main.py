from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with  open('data.json', mode='r') as data_file:
            data = json.load(data_file)

        
    except FileNotFoundError:
        messagebox.showerror(title='error', message='file isnot found')
    else:    
        if website in data:
                email = data[website]['email']
                password = data[website]['password']
                messagebox.showinfo(title='your website info', message=f"email: {email}\n password: {password}"
                                    )



def create_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)



    password_letters = [(random.choice(letters)) for char in range(nr_letters)]
    password_symnols = [(random.choice(symbols)) for char in range(nr_symbols)]
    password_numbers = [(random.choice(numbers)) for char in range(nr_numbers)]

    password_list =  password_letters + password_numbers + password_symnols
    


    random.shuffle(password_list)


    password = ''.join(password_list)
    password_entry.inser4t(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()

    new_data = {
        website: {
            'email': email,
            'password': password,
        }
    }

    if website == '' or password == '':
        messagebox.showwarning(title="error", message="you left some fields empty")
    else:
        try:
            with open('data.json', mode='r') as data_file:
                # reading the old data
                data = json.load(data_file)
        except FileNotFoundError:
                with open('data.json', mode='w') as data_file:
                    json.dump(new_data, data_file, indent=4)
        else:
            # update the data
            data.update(new_data)
            with open('data.json', mode='w') as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)


        finally:
            website_entry.delete(0, END)    
            password_entry.delete(0, END)      



# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("Password Manager")
windows.config(padx=20, pady=20)

canvas = Canvas(width=200, height=189)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

website_entry = Entry(width=21)
website_entry.grid(row=1,  column=1)
website_entry.focus()

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(row=2, columnspan=2, column=1)
email_entry.insert(0, 'anishgharti10@gmail.com')


password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

password_entry = Entry(width=35)
password_entry.grid(row=3,  column=1, columnspan=2)

password_button = Button(text='create Password', command=create_password)
password_button.grid(column=2, row=3, )


add_button = Button(text='Add', width=35, command=save)
add_button.grid(row=4, columnspan=2, column=1)


search_button = Button(text='Search', command=find_password)
search_button.grid(row=1, column=2)

windows.mainloop()





 # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail:{email} \nPassword:{password}   ")
        # if is_ok:
            # with open('data.txt', mode='a') as data_file:
            #     data = data_file.write(f"{website} !! {email} !! {password} \n")

            #     website_entry.delete(0, END)
            #     password_entry.delete(0, END)