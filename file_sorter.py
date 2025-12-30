#! python3
# file_sorter.py - A program to sort files in a directory into folders based on file extensions.

import os, shutil

FILE_MAPPING = {
    'Documents': ['.pdf', '.txt', '.html', '.css', '.js', '.py', '.pbix', '.csv', '.epub', '.docx', '.xlsx', '.ipynb', '.json', '.md', '.yaml', '.log', '.ppix'],
    'Images': ['.jpeg', '.jpg', '.png', '.gif', '.svg', '.jfif', '.webp', '.ico', '.heic', '.bmp'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.3gp', '.flv'],
    'Music': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Programs': ['.exe', '.msi', '.bat', '.sh', '.apk'],
}  # Dictionary to map files according to extension. Might update later...

def relocate(source: str, ext: str, root_path: str, checked_folders: set):
    "Moves files from source to destination based on their extensions."
    folder = get_target_folder(ext)
    dest_folder = os.path.join(root_path, folder)
    # Create the destination if hasn't been created before
    if folder not in checked_folders:
        checked_folders.add(folder)
        os.makedirs(dest_folder, exist_ok=True)
    
    file_name = os.path.basename(source)
    name_only, extension = os.path.splitext(file_name)
    dest_path = os.path.join(dest_folder, file_name)

    # Helps to rename files if a file with the same name is already in destination
    counter = 1
    while os.path.exists(dest_path):
        new_name = f"{name_only}_{counter}{extension}"
        dest_path = os.path.join(dest_folder, new_name)
        counter += 1

    # Move the file
    shutil.move(source, dest_path)
    print(f'Moved: {source} --> {dest_path}')

def get_target_folder(ext: str) -> str:
    "Helps to determine the folder that a file belongs to based on extension."
    for folder, extensions in FILE_MAPPING.items():
        if ext in extensions:
            return folder
    return 'Others'

def main():
    "Runs the main program by looping through all files in SOURCE_PATH."
    checked_folders = set()  # To keep track of created folders
    SOURCE_PATH = input("Enter the path of the folder to clean up: ")

    # Input validation
    if not os.path.exists(SOURCE_PATH):
        print(f"Error: The path {SOURCE_PATH} does not exist.")
        return
    if not os.path.isdir(SOURCE_PATH):
        print(f"Error: The path {SOURCE_PATH} is a file, not a folder.")
        return
    
    # loop through all files in the source folder
    files = os.listdir(SOURCE_PATH)
    for file_name in files:
        full_path = os.path.join(SOURCE_PATH, file_name)
        if not os.path.isdir(full_path):
            ext = os.path.splitext(file_name)[1].lower()
            relocate(full_path, ext, SOURCE_PATH, checked_folders)

if __name__ == '__main__':
    main()