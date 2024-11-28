import os
import time
from tkinter import Tk, Label, Button, Entry, messagebox, StringVar, Listbox, Scrollbar, END, Frame
from datetime import datetime

# File paths and settings
HOSTS_FILE = "/etc/hosts" if os.name != "nt" else r"C:\Windows\System32\drivers\etc\hosts"
REDIRECT = "127.0.0.1"
PASSWORD = "admin123"  # Default password
BLOCK_START = 9  # Blocking starts at 9:00 AM
BLOCK_END = 17  # Blocking ends at 5:00 PM

# GUI variables
root = Tk()#tkinter
root.title("Website & App Blocker")#tilte
root.geometry("500x550")#size of box
root.configure(bg="#f0f0f0")#background colour

status_var = StringVar()
status_var.set("Status: Idle")
log_var = StringVar()

# Website and app lists
websites = ["www.facebook.com", "facebook.com", "www.youtube.com", "youtube.com", "www.gmail.com" , "gmail.com"]
apps = ["notepad.exe", "chrome.exe"]

# Helper functions
def block_websites():
    """Block websites by modifying the hosts file."""
    with open(HOSTS_FILE, "r+") as file:
        content = file.read()
        for website in websites:
            if website not in content:
                file.write(f"{REDIRECT} {website}\n")
    log_action("Websites Blocked")
    status_var.set("Status: Websites Blocked")

def unblock_websites():
    """Unblock websites by removing them from the hosts file."""
    with open(HOSTS_FILE, "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if not any(website in line for website in websites):
                file.write(line)
        file.truncate()
    log_action("Websites Unblocked")
    status_var.set("Status: Websites Unblocked")

def schedule_blocking():
    """Schedule website and app blocking during specified hours."""
    current_hour = datetime.now().hour
    if BLOCK_START <= current_hour < BLOCK_END:
        block_websites()
        status_var.set("Status: Blocking Active")
        log_action("Scheduled Blocking Activated")
        messagebox.showinfo("Blocking Active", "Websites and apps are blocked!")
    else:
        unblock_websites()
        status_var.set("Status: Blocking Inactive")
        log_action("Scheduled Blocking Deactivated")
        messagebox.showinfo("Blocking Inactive", "Websites and apps are unblocked!")

def log_action(action):
    """Log actions in the GUI."""
    log_list.insert(END, f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {action}")

def handle_password(action):
    """Prompt user for a password before performing sensitive actions."""
    password = password_entry.get()
    if password == PASSWORD:
        if action == "block":
            block_websites()
        elif action == "unblock":
            unblock_websites()
        elif action == "schedule":
            schedule_blocking()
    else:
        messagebox.showerror("Access Denied", "Incorrect password!")

def add_website():
    """Add a website to the block list."""
    new_website = website_entry.get()
    if new_website and new_website not in websites:
        websites.append(new_website)
        log_action(f"Added website: {new_website}")
        website_entry.delete(0, END)

# GUI Layout
Label(root, text="Website & App Blocker", font=("Helvetica", 16, "bold"), bg="#f0f0f0").pack(pady=10)

frame = Frame(root, bg="#f0f0f0")
frame.pack(pady=5)

Label(frame, text="Enter Password:", bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5)
password_entry = Entry(frame, show="*", width=20)
password_entry.grid(row=0, column=1, padx=5, pady=5)

Button(root, text="Block Websites", command=lambda: handle_password("block"), width=20,
       bg="#ff6961", fg="white").pack(pady=5)  # Red button
Button(root, text="Unblock Websites", command=lambda: handle_password("unblock"), width=20,
       bg="#77dd77", fg="white").pack(pady=5)  # Green button
Button(root, text="Schedule Blocking", command=lambda: handle_password("schedule"), width=20,
       bg="#fdfd96", fg="black").pack(pady=5)  # Yellow button

Label(root, text="Add Website to Block:", bg="#f0f0f0").pack(pady=5)
website_entry = Entry(root, width=40)
website_entry.pack(pady=5)
Button(root, text="Add Website", command=add_website, width=20,
       bg="#aec6cf", fg="white").pack(pady=5)  # Blue button

Label(root, text="Action Log:", bg="#f0f0f0").pack(pady=10)
log_frame = Frame(root)
log_frame.pack(pady=5)
scrollbar = Scrollbar(log_frame)
scrollbar.pack(side="right", fill="y")
log_list = Listbox(log_frame, width=50, height=10, yscrollcommand=scrollbar.set)
log_list.pack(side="left")
scrollbar.config(command=log_list.yview)

Label(root, textvariable=status_var, fg="green", bg="#f0f0f0").pack(pady=20)
Button(root, text="Exit", command=root.quit, width=10,
       bg="#d3d3d3", fg="black").pack(pady=10)  # Grey button

# Run the app
root.mainloop()
