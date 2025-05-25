import tkinter as tk
from tkinter import messagebox, simpledialog
import subprocess
import os
import requests

# -------------------------- TOOL PATHS --------------------------
tool_paths = {
    "Tool 1": {
        "path": "C:\\Users\\DRR8656\\Desktop\\my_tool_launcher\\tools\\GANG-Nuker\\GANG.py",
        "desc": "Powerful gang nuker script"
    },
    "Tool 2": {
        "path": "C:\\Users\\DRR8656\\Desktop\\my_tool_launcher\\tools\\LithiumNukerV2-main\\LithiumNukerV2.exe",
        "desc": "Fast Lithium Nuker executable"
    },
    "Tool 3": {
        "path": "tools\\tool3.py",
        "desc": "Utility tool number three"
    },
    "Tool 4": {
        "path": "tools\\tool4.py",
        "desc": "Fourth tool with advanced features"
    },
    "Tool 5": {
        "path": "tools\\tool5.py",
        "desc": "Fifth tool for special tasks"
    }
}

# -------------------------- STYLES --------------------------
BG_COLOR = "#000000"
TEXT_COLOR = "#00FF00"
BTN_COLOR = "#003300"
BTN_HOVER = "#005500"
FONT = ("Courier New", 20, "bold")
TITLE_FONT = ("Courier New", 26, "bold")

# -------------------------- USER CREDENTIALS --------------------------
# Define your users and passwords here
USER_DATA = {
    "Alketbi": "Ali_moh69",
    "Dark": "Dark973",
    # add more users here
}

# Discord webhook URL (put your actual webhook URL here)
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1376274904252551219/XXY9OHEno6SkL_ntplsn_Cs1fzcg1OzGgEfMBPHiF_x_sEUw85CuZ79ljmqz-4OY0zaz"

# -------------------------- FUNCTIONS --------------------------

def run_tool(path):
    if not os.path.exists(path):
        messagebox.showerror("Error", f"Tool not found:\n{path}")
        return

    ext = os.path.splitext(path)[1].lower()
    if ext == '.py':
        subprocess.Popen(['cmd', '/c', 'start', 'python', path])
    else:
        subprocess.Popen(['cmd', '/c', 'start', path])

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

def send_forgot_password_to_discord(username):
    content = f"User requested password reset: **{username}**"
    data = {"content": content}
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=data)
        response.raise_for_status()
        return True
    except Exception as e:
        print("Failed to send webhook:", e)
        return False

def forgot_password():
    username = simpledialog.askstring("Forgot Password", "Enter your username:")
    if not username:
        return
    if username in USER_DATA:
        success = send_forgot_password_to_discord(username)
        if success:
            messagebox.showinfo("Forgot Password", f"Your username '{username}' has been sent to support via Discord.")
        else:
            messagebox.showerror("Error", "Failed to notify support. Try again later.")
    else:
        messagebox.showerror("Error", "Username not found.")

def check_credentials():
    username = username_entry.get()
    password = password_entry.get()

    if USER_DATA.get(username) == password:
        show_welcome_screen(username)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")
        password_entry.delete(0, tk.END)

# -------------------------- SCREENS --------------------------

def show_login_screen():
    clear_window()
    label = tk.Label(root, text="Login to Alketbi Launcher", font=TITLE_FONT, fg=TEXT_COLOR, bg=BG_COLOR)
    label.pack(pady=30)

    global username_entry, password_entry
    frame = tk.Frame(root, bg=BG_COLOR)
    frame.pack(pady=10)

    tk.Label(frame, text="Username:", fg=TEXT_COLOR, bg=BG_COLOR, font=FONT).grid(row=0, column=0, sticky="e", padx=5, pady=5)
    username_entry = tk.Entry(frame, font=FONT, width=20)
    username_entry.grid(row=0, column=1, padx=5, pady=5)
    username_entry.focus()

    tk.Label(frame, text="Password:", fg=TEXT_COLOR, bg=BG_COLOR, font=FONT).grid(row=1, column=0, sticky="e", padx=5, pady=5)
    password_entry = tk.Entry(frame, show="*", font=FONT, width=20)
    password_entry.grid(row=1, column=1, padx=5, pady=5)

    login_btn = tk.Button(
        root,
        text="Login",
        font=FONT,
        fg=TEXT_COLOR,
        bg=BTN_COLOR,
        activebackground=BTN_HOVER,
        width=20,
        height=2,
        borderwidth=0,
        command=check_credentials
    )
    login_btn.pack(pady=10)

    forgot_btn = tk.Button(
        root,
        text="Forgot Password?",
        font=("Courier New", 12, "underline"),
        fg=TEXT_COLOR,
        bg=BG_COLOR,
        borderwidth=0,
        command=forgot_password
    )
    forgot_btn.pack()

def show_welcome_screen(username):
    clear_window()
    label = tk.Label(root, text=f"Hello {username}", font=TITLE_FONT, fg=TEXT_COLOR, bg=BG_COLOR)
    label.pack(pady=100)

    start_btn = tk.Button(
        root,
        text=">> START <<",
        font=FONT,
        fg=TEXT_COLOR,
        bg=BTN_COLOR,
        activebackground=BTN_HOVER,
        width=20,
        height=2,
        borderwidth=0,
        command=show_tool_menu
    )
    start_btn.pack()

def show_tool_menu():
    clear_window()
    title = tk.Label(root, text="🛠 TOOL MENU 🛠", font=TITLE_FONT, fg=TEXT_COLOR, bg=BG_COLOR)
    title.pack(pady=20)

    frame = tk.Frame(root, bg=BG_COLOR)
    frame.pack()

    for idx, tool_name in enumerate(tool_paths):
        tool_info = tool_paths[tool_name]
        path = tool_info["path"]
        desc = tool_info["desc"]

        tool_frame = tk.Frame(frame, bg=BG_COLOR, pady=10)
        tool_frame.grid(row=idx, column=0, padx=20, pady=10, sticky="w")

        btn = tk.Button(
            tool_frame,
            text=tool_name,
            font=FONT,
            fg=TEXT_COLOR,
            bg=BTN_COLOR,
            activebackground=BTN_HOVER,
            width=20,
            height=2,
            borderwidth=0,
            command=lambda p=path: run_tool(p)
        )
        btn.pack()

        desc_label = tk.Label(
            tool_frame,
            text=desc,
            font=("Courier New", 12, "italic"),
            fg=TEXT_COLOR,
            bg=BG_COLOR,
            wraplength=300,
            justify="left"
        )
        desc_label.pack(pady=5)

    back_btn = tk.Button(
        root,
        text="<< Back",
        font=("Courier New", 16),
        fg=TEXT_COLOR,
        bg=BTN_COLOR,
        activebackground=BTN_HOVER,
        width=15,
        height=1,
        command=show_welcome_screen
    )
    back_btn.pack(pady=20)

# -------------------------- START --------------------------
root = tk.Tk()
root.title("Alketbi Hacker Launcher")
root.geometry("800x600")
root.config(bg=BG_COLOR)

show_login_screen()
root.mainloop()
