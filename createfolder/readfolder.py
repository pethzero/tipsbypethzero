import os

def list_folders_and_files(folder_path, output_file='folder_contents.txt'):
    with open(output_file, 'w') as file:
        for root, dirs, files in os.walk(folder_path):
            # Write the current folder path to the file
            file.write(f"Folder: {root}\n")
            
            # Write all files in the current folder to the file
            for file_name in files:
                file_base, file_extension = os.path.splitext(file_name)
                file.write(f"File: {os.path.join(root, file_name)}\n")
                print(file_name)

mode = 2

current_folder = os.getcwd()
current_folder_manual = r"D:\TEST\tipsbypethzero\createfolder\pic"

if mode == 1:
    list_folders_and_files(current_folder)
elif mode == 2:
    list_folders_and_files(current_folder_manual)
elif mode == 3:
    list_folders_and_files(current_folder_manual)





