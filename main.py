"""
day 28 of 100 days of code, Making a password manager
To have some extra fun this is one of the worst password managers ever.
It generates vulnerable passwords and stores them in a plain text file, with login, and website
"""
import string
import tkinter as tk
from tkinter import messagebox
from random import choice, shuffle
from pyperclip import copy

FONT = ("Arial", 15)
SMALL_FONT = ("Arial", 10)

# ------- Saving function ------ #
def save_password():
    # get the values from the entries
    site = website_entry.get().strip()
    user = login_entry.get().strip()
    password = password_entry.get().strip()

    if site == '' or user == '' or password == '':
        messagebox.showerror(title="Error", message="Oops! You left some fields blank.")

    else:
        # confirm the entry
        is_ok = messagebox.askokcancel(title="Save this info?",
                                       message=f"WEBSITE: {site}\nUSER: {user}\nPASSWORD: {password}\n\nSave in plain text so everyone can read it?")
        if is_ok:
            # write the entry to the file
            with open("mypassword.txt", "a") as f:
                f.write(f"\n{user},{password},{site}")

            # clear out the entries
            password_entry.delete(0, tk.END)
            login_entry.delete(0, tk.END)
            website_entry.delete(0, tk.END)


# ------- Password Generation ------ #
common_password_parts = ['pa$$word', 'letmein', '123', '321', '666', 'iloveyou', 'admin', 'Admin', 'ADMIN', '365', '247', '2020','Windows', 'Williams', 'lovely',
                         '420', '69', 'monkey', '1234567890', 'PASS', 'WORD', 'God', 'test', 'Test', 'baseball', 'G0D', '1991', '$$$', 'Google', 'Jennifer', 'Babygirl!', 'baby',
                         '90210', '1989', '2021', 'asdfg', 'zxcv', 'icecream', 'sunshine','wordpass', 'secret', 'bingo', 'mutt', 'weed', 'Amazon', 'Andrew', '11111111', '8675309',
                         'gold', 'm0ney', 'happy' 'chocolate', 'Princess','cat', 'John', 'Mathew', 'Mark', 'Luke', 'Mary', 'Jesus', 'Qwerty', '!', '99', 'Swift', 'asdfghjkl',
                         'funky', 'f00tball!', 'Football','basketball!', '111', '222', '333', '444', '555', '2022', '2023', '2024', 'love', 'dubsmash', 'w0rd', 'Taylor', 'fish', 'silver',
                         '777', '888', '999', '000', 'aaa', 'AAAA', 'AAA', '0987654321', '7', '13', 'sexy', 'daddy', 'mommy', 'Flower', 'Whatever', '87654321', 'beer', 'steak']

letters = string.ascii_lowercase + string.ascii_uppercase
numbers = string.digits
chars = ['!', '$', '&', '*', '#', '?', '@', '.']


def generate_password():
    current_mode = mode.get()
    password_entry.delete(0, tk.END)

    if current_mode == "trash":
        new_password = choice(common_password_parts)

        while len(new_password) < 7:
            new_password = new_password + choice(common_password_parts)
            if len(new_password) > 13:
                new_password = choice(common_password_parts)

    else:
        pass_letters = [choice(letters) for _ in range(3,5)]
        pass_numbers = [choice(numbers) for _ in range(1,3)]
        pass_chars = [choice(chars) for _ in range(1,2)]

        character_list = pass_letters + pass_numbers + pass_chars
        shuffle(character_list)
        new_password = "".join(character_list)

    # populate the password field and copy the password to clipboard
    password_entry.insert(0, new_password)
    copy(new_password)


# ---- Building the UI ---- #
window = tk.Tk()
window.title("Tr@sh.Pa$$")
window.config(padx=20, pady=20)

# lock logo setup for grid
canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
lock_img = tk.PhotoImage(file="broken_lock.png")
canvas.create_image(100, 100, image=lock_img)


# row 0
canvas.grid(row=0, column=0, columnspan=3)


# row 1
website_label = tk.Label(text="Website: ", font=(FONT))
website_label.grid(row=1, column=0)
website_entry = tk.Entry(width=36)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
# .focus puts the cursor into the entry when the app launches

# row 2
login_label = tk.Label(text="Login: ", font=(FONT))
login_label.grid(row=2, column=0)
login_entry = tk.Entry(width=36)
login_entry.grid(row=2, column=1, columnspan=2)
login_entry.insert(0, "fake_email@fake.bs")

# row 3
password_label = tk.Label(text="Password: ", font=(FONT))
password_label.grid(row=3, column=0)
password_entry = tk.Entry(width=18)
password_entry.grid(row=3, column=1)
generate_password_button = tk.Button(text="Generate", command=generate_password, width=14)
generate_password_button.grid(row=3, column=2)

# row 4
mode = tk.StringVar()
trash = tk.Radiobutton(text="Too Weak", variable=mode, value="trash", width=16)
better = tk.Radiobutton(text="Too Short", variable=mode, value="better", width=16)
trash.grid(row=4, column=1)
better.grid(row=4, column=2)

#row 5
add_password_button = tk.Button(text="Save", width=34, command=save_password)
add_password_button.grid(row=5, column=1, columnspan=2)

#row 6
info_label = tk.Label(text="Trash Passwords automatically copied to clipboard", font=(SMALL_FONT))
info_label.grid(row=6, column=1, columnspan=2)

window.mainloop()
