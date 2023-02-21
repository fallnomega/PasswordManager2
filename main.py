import tkinter as tk
from tkinter import messagebox
import random

global my_new_password


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    options = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!',
               '#', '$', '%', '&', '(', ')', '*', '+']
    total_char = len(password_entry.get())
    total_letters = 0
    end = True
    new_password = []

    while end:
        for x in range(total_char):
            char_option = random.randint(0, 70)
            new_password.append(options[char_option])
            if len(new_password) == total_char:
                end = False

    my_new_password = ''.join(new_password)
    password_entry.delete(0, 'end')

    password_entry.insert(0, my_new_password)
    # print(my_new_password)
    # new_pass_windows = tk.messagebox()


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    temp_password = password_entry.get()
    temp_url = url_entry.get()
    temp_user = email_or_user_entry.get()
    if len(temp_password) == 0 or len(temp_user) == 0 or len(temp_url) == 0:
        messagebox.showerror(title="Error",
                             message=f"These fields should no be blank")
    else:
        print(temp_password)
        is_okay_to_save = messagebox.askokcancel(title=temp_url,
                                                 message=f"{temp_url}\n{temp_user}\n{temp_password}\nSave to file ? ")
        # print(my_new_password)
        if is_okay_to_save:
            with open("password_list.txt", 'a+') as file:
                file.write(f"{temp_url} | {temp_user} | {temp_password}\n")
                file.close()
            password_entry.delete(0, 'end')
            url_entry.delete(0, 'end')
            email_or_user_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title = "Password Manager"
window_background = tk.PhotoImage(file="logo.png")
window.config(padx=20, pady=20)
canvas = tk.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=window_background)
canvas.grid(row=0, column=1)

url = tk.Label(text="Website: ")
url.grid(row=1, column=0)
url_entry = tk.Entry(bg="white", borderwidth=2, width=35)
url_entry.grid(row=1, column=1, columnspan=2)
url_entry.insert(0, "www.amazon.com")

email_or_user = tk.Label(text="Email/Username: ")
email_or_user.grid(row=2, column=0)
email_or_user_entry = tk.Entry(bg="white", borderwidth=2, width=35)
email_or_user_entry.grid(row=2, column=1, columnspan=2)
email_or_user_entry.insert(0, "my_email_address@domain.com")

password = tk.Label(text="Password: ")
password.grid(row=3, column=0)
password_entry = tk.Entry(bg="white", borderwidth=2, width=21)
password_entry.grid(row=3, column=1)
password_entry.insert(0, "MyCoolPassword")

gen_pass = tk.Button(text="Generate Password", command=generate_password)
gen_pass.grid(row=3, column=2)

add_pass = tk.Button(text="Add", width=36, command=save_password)
add_pass.grid(row=4, column=1, columnspan=2)

window.mainloop()