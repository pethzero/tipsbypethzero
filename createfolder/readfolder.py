import os

# อ่านรายชื่อโฟลเดอร์จากไฟล์ folder_list.txt
with open('folder_list.txt', 'r') as file:
    folder_names = file.read().splitlines()

# สร้างโฟลเดอร์ตามรายชื่อใน folder_names
for folder_name in folder_names:
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
