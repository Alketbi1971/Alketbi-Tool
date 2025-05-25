import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import random
from PIL import Image, ImageTk, ImageSequence
import requests  # Added for webhook

# -------------------------- TOOL PATHS --------------------------
# Base directory of the launcher (auto-detects current directory)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# -------------------------- TOOL PATHS --------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

tool_paths = {
    "Tool 1": {
        "path": os.path.join(BASE_DIR, "tools", "GANG-Nuker", "GANG.py"),
        "desc": "Powerful gang nuker script"
    },
    "Tool 2": {
        "path": os.path.join(BASE_DIR, "tools", "LithiumNukerV2-main", "LithiumNukerV2.exe"),
        "desc": "Fast Lithium Nuker executable"
    },
    "Tool 3": {
        "path": os.path.join(BASE_DIR, "tools", "tool3.py"),
        "desc": "Utility tool number three"
    },
    "Tool 4": {
        "path": os.path.join(BASE_DIR, "tools", "tool4.py"),
        "desc": "Fourth tool with advanced features"
    },
    "Tool 5": {
        "path": os.path.join(BASE_DIR, "tools", "tool5.py"),
        "desc": "Fifth tool for special tasks"
    }
}
USER_DATA = {
    "root": "Ali_moh69",
    "Dark": "Dark973",
}

BG_COLOR = "#000000"
TEXT_COLOR = "#00FF00"
BTN_COLOR = "#003300"
BTN_HOVER = "#005500"
FONT = ("Courier New", 20, "bold")
TITLE_FONT = ("Courier New", 26, "bold")

current_user = None

root = tk.Tk()
root.title("Alketbi Hacker Launcher")

# Fullscreen mode
root.attributes("-fullscreen", True)
root.configure(bg=BG_COLOR)

# GIF animation variables (not used, GIF removed)
gif_frames = []
gif_index = 0
gif_label = None

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

def check_credentials():
    global current_user
    username = username_entry.get()
    password = password_entry.get()

    if USER_DATA.get(username) == password:
        current_user = username
        show_welcome_screen()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")
        password_entry.delete(0, tk.END)

WEBHOOK_URL = "https://discord.com/api/webhooks/1376274904252551219/XXY9OHEno6SkL_ntplsn_Cs1fzcg1OzGgEfMBPHiF_x_sEUw85CuZ79ljmqz-4OY0zaz"

def random_color():
    return f'#{random.randint(0, 0xFFFFFF):06x}'

def forgot_password():
    username = username_entry.get()
    if username.strip() == "":
        messagebox.showinfo("Forgot Password", "Please enter your username first.")
        return
    
    # Send a message to Discord webhook
    data = {
        "content": f"Password recovery requested for username: {username}"
    }
    try:
        requests.post(WEBHOOK_URL, json=data)
    except Exception as e:
        print(f"Failed to send webhook: {e}")

    messagebox.showinfo("Forgot Password", f"Password recovery info for '{username}' would be sent.")

def show_login_screen():
    clear_window()
    root.config(bg=BG_COLOR)

    label = tk.Label(root, text="Enter Username", font=TITLE_FONT, fg=TEXT_COLOR, bg=BG_COLOR)
    label.pack(pady=20)

    global username_entry
    username_entry = tk.Entry(root, font=FONT, width=30)
    username_entry.pack(pady=5)
    username_entry.focus()

    label2 = tk.Label(root, text="Enter Password", font=TITLE_FONT, fg=TEXT_COLOR, bg=BG_COLOR)
    label2.pack(pady=20)

    global password_entry
    password_entry = tk.Entry(root, show="*", font=FONT, width=30)
    password_entry.pack(pady=5)

    submit_btn = tk.Button(
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
    submit_btn.pack(pady=10)

    forgot_btn = tk.Button(
        root,
        text="Forgot Password?",
        font=("Courier New", 14, "underline"),
        fg="#00FFFF",
        bg=BG_COLOR,
        borderwidth=0,
        cursor="hand2",
        command=forgot_password
    )
    forgot_btn.pack()

def show_welcome_screen():
    clear_window()
    root.config(bg=BG_COLOR)

    # Simple welcome screen with text label only (no GIF)
    text_label = tk.Label(root, text="1337 Team", font=("Courier New", 48, "bold"), bg=BG_COLOR)
    text_label.place(relx=0.5, rely=0.3, anchor="center")

    def change_color():
        text_label.config(fg=random_color())
        root.after(500, change_color)
    change_color()

    start_btn = tk.Button(
        root,
        text=">> START <<",
        font=FONT,
        fg="#FFFFFF",
        bg="#222222",
        activebackground="#555555",
        width=20,
        height=2,
        borderwidth=0,
        command=show_tool_menu
    )
    start_btn.place(relx=0.5, rely=0.5, anchor="center")

def show_tool_menu():
    clear_window()
    root.config(bg=BG_COLOR)

    title = tk.Label(root, text="🛠 TOOL MENU 🛠", font=TITLE_FONT, fg=TEXT_COLOR, bg=BG_COLOR)
    title.pack(pady=10)

    canvas = tk.Canvas(root, bg=BG_COLOR, highlightthickness=0)
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg=BG_COLOR)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    for idx, tool_name in enumerate(tool_paths):
        tool_info = tool_paths[tool_name]
        path = tool_info["path"]
        desc = tool_info["desc"]

        tool_frame = tk.Frame(scrollable_frame, bg=BG_COLOR, pady=10)
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
    back_btn.pack(pady=10)

def exit_fullscreen(event=None):
    root.attributes("-fullscreen", False)

root.bind("<Escape>", exit_fullscreen)

show_login_screen()
root.mainloop()
