import os

text_name = 'folder_list.txt'

# อ่านรายชื่อโฟลเดอร์จากไฟล์ folder_list.txt
with open(text_name, 'r') as file:
    folder_names = file.read().splitlines()

mode = 1
# สร้างโฟลเดอร์ตามรายชื่อใน folder_names
if mode == 1:
    for folder_name in folder_names:
        if not os.path.exists(folder_name):
            try:
                os.makedirs(folder_name)
                print(f"Created folder: {folder_name}")
            except OSError as e:
                print(f"Error: {folder_name} : {e.strerror}")
        else:
            print(f"Folder already exists: {folder_name}")
else:
    for folder_name in folder_names:
        if not os.path.exists(folder_name):
            try:
                os.makedirs(folder_name)
                print(f"Created folder: {folder_name}")
            except OSError as e:
                print(f"Error: {folder_name} : {e.strerror}")
        else:
            print(f"Folder already exists: {folder_name}")