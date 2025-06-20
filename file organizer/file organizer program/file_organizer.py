import os
import shutil


TARGET_FOLDER = input("Enter the path of the folder to organize: ")   # add folder path to organize

FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css"]
}

def create_folder(folder_name):
    folder_path = os.path.join(TARGET_FOLDER, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

def move_file(file, dest_folder):
    try:
        shutil.move(file, dest_folder)
    except Exception as e:
        print(f"Error moving file {file}: {e}")

def organize():
    for filename in os.listdir(TARGET_FOLDER):
        file_path = os.path.join(TARGET_FOLDER, filename)

        
        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(filename)
        moved = False

        for folder_name, extensions in FILE_TYPES.items():
            if ext.lower() in extensions:
                dest_folder = create_folder(folder_name)
                move_file(file_path, dest_folder)
                moved = True
                break

        
        if not moved:
            other_folder = create_folder("Others")
            move_file(file_path, other_folder)

    print("✅ Folder organized successfully!")

if __name__ == "__main__":
    organize()
