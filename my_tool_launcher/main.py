import tkinter as tk
from tkinter import messagebox
import subprocess
import os

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

# -------------------------- PASSWORD --------------------------
PASSWORD = "your_password_here"  # Change this to your actual password

# -------------------------- MAIN WINDOW --------------------------
root = tk.Tk()
root.title("Alketbi Hacker Launcher")
root.geometry("800x600")
root.config(bg=BG_COLOR)

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

def check_password():
    entered = password_entry.get()
    if entered == PASSWORD:
        show_welcome_screen()
    else:
        messagebox.showerror("Error", "Incorrect password, try again.")
        password_entry.delete(0, tk.END)

def show_login_screen():
    clear_window()
    label = tk.Label(root, text="Enter Password", font=TITLE_FONT, fg=TEXT_COLOR, bg=BG_COLOR)
    label.pack(pady=80)

    global password_entry
    password_entry = tk.Entry(root, show="*", font=FONT, width=30)
    password_entry.pack(pady=10)
    password_entry.focus()

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
        command=check_password
    )
    submit_btn.pack(pady=20)

def show_welcome_screen():
    clear_window()
    label = tk.Label(root, text="Hello Alketbi", font=TITLE_FONT, fg=TEXT_COLOR, bg=BG_COLOR)
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
show_login_screen()
root.mainloop()
