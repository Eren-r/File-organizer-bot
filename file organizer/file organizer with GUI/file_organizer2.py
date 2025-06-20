import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css"]
}

def create_folder(folder_name, base_path):
    folder_path = os.path.join(base_path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

def move_file(file, dest_folder):
    try:
        shutil.move(file, dest_folder)
    except Exception as e:
        print(f"Error moving file {file}: {e}")

def organize(target_folder):
    for filename in os.listdir(target_folder):
        file_path = os.path.join(target_folder, filename)

        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(filename)
        moved = False

        for folder_name, extensions in FILE_TYPES.items():
            if ext.lower() in extensions:
                dest_folder = create_folder(folder_name, target_folder)
                move_file(file_path, dest_folder)
                moved = True
                break

        if not moved:
            other_folder = create_folder("Others", target_folder)
            move_file(file_path, other_folder)

    messagebox.showinfo("Success", "✅ Folder organized successfully!")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    folder_path.set(folder_selected)

def start_organizing():
    path = folder_path.get()
    if os.path.exists(path):
        organize(path)
    else:
        messagebox.showerror("Error", "Please select a valid folder.")

# GUI Setup
window = tk.Tk()
window.title("File Organizer Bot")
window.geometry("400x200")

folder_path = tk.StringVar()

tk.Label(window, text="Select folder to organize:", font=("Arial", 12)).pack(pady=10)
tk.Entry(window, textvariable=folder_path, width=40).pack()
tk.Button(window, text="Browse", command=browse_folder).pack(pady=5)
tk.Button(window, text="Start Organizing", command=start_organizing, bg="green", fg="white").pack(pady=20)

window.mainloop()
