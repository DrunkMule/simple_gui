import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Login")
root.geometry("800x500")

# Global variables
tries = 0
login_frame = None
new_frame = None
new_label = None

def login():
    global login_frame, new_frame, new_label

    username = entry1.get()
    password = entry2.get()

    if is_valid_account(username, password):
        print("Login successful")
        login_frame.pack_forget()  # Hide the login frame
        open_new_page()
    else:
        print("Invalid Password")

def signup():
    username = entry1.get()
    password = entry2.get()

    if username_exists(username):
        print("Username already exists")
    else:

        with open("user_data.txt", "a") as file:
            file.write(f"{username}:{password}\n")
            print("Signup:", username, password)

def is_valid_account(username, password):
    with open("user_data.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(":")
            if username == stored_username and password == stored_password:
                return True
    return False

def username_exists(username):
    with open("user_data.txt", "r") as file:
        for line in file:
            stored_username, _ = line.strip().split(":")
            if username == stored_username:
                return True
    return False

def open_new_page():
    global new_frame, new_label

    new_frame = customtkinter.CTkFrame(master=root)
    new_frame.pack(pady=20, padx=60, fill="both", expand=True)

    new_label = customtkinter.CTkLabel(master=new_frame, text="Welcome to the New Page", font=("default", 24))
    new_label.pack()

# Create the login frame
login_frame = customtkinter.CTkFrame(master=root)
login_frame.pack(pady=20, padx=60, fill="both", expand=True)

label_frame = customtkinter.CTkFrame(master=login_frame)
label_frame.pack(pady=12, padx=10)

label = customtkinter.CTkLabel(master=label_frame, text="Login System", font=("default", 24))
label.pack()

entry1 = customtkinter.CTkEntry(master=login_frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=login_frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

login_button = customtkinter.CTkButton(master=login_frame, text="Login", command=login)
login_button.pack(pady=12, padx=10)

signup_button = customtkinter.CTkButton(master=login_frame, text="Signup", command=signup)
signup_button.pack(pady=12, padx=10)

root.mainloop()
