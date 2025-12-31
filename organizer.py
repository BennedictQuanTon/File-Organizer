import os
import shutil
# This dictionary tells Python which folders to create for which extensions
DIRECTORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov"]
}
def start_organizing():
    # 1. Ask the user for the folder path
    path = input("Enter the path of the folder you want to clean: ")

    # 2. Go into that folder
    os.chdir(path)
    # 3. Loop through every file in that folder
    for file in os.listdir():
        # Get the file extension (like .jpg)
        file_name, extension = os.path.splitext(file)
        
        # 4. Check our dictionary to see where this extension belongs
        for folder_name, extensions_list in DIRECTORIES.items():
            if extension.lower() in extensions_list:
                
                # Create the folder if it doesn't exist yet
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                
                # Move the file into that folder
                shutil.move(file, f"{folder_name}/{file}")
                print(f"Successfully moved {file} to {folder_name}")

# Run the function
start_organizing()