import os

def list_folders(directory):
    return [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]

def delete_folder(folder_path):
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))
    os.rmdir(folder_path)

def process_folders(folder_path, group):
    for item in group:
        folder_main = os.path.join(folder_path, str(item['x']))
        folder_sub = os.path.join(folder_path, str(item['x']), str(item['y']))
        folders = list_folders(folder_main)
        for folder in folders:
            if folder != str(item['y']):
                delete_folder(os.path.join(folder_main, folder))

mode = 1
if mode == 1:
    current_folder = os.path.join(os.getcwd() , 'pic')
else:
    current_folder = r"D:\TEST\tipsbypethzero\createfolder\process_delete\pic"

group = [{"x": 1, "y": 5}]
process_folders(current_folder, group)
