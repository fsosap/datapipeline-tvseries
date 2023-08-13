import glob
import os

def clear_files_from_directory(dir:str):
    """code from: https://sparkbyexamples.com/python/how-to-delete-file-or-folder-in-python/#:~:text=an%20Empty%20Folder-,The%20os.,method%20will%20raise%20an%20OSError."""
    file_list = glob.glob(dir + '*')
    for file_path in file_list:
        try:
            os.remove(file_path)
            print(f"{file_path} deleted successfully.")
        except OSError as e:
            print(f"Error: {file_path} : {e.strerror}")