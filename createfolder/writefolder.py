import os

current_directory = os.getcwd()  # รับตำแหน่งปัจจุบันของ Python
folder_list = os.listdir(current_directory)  # รับรายชื่อไดเรกทอรีในตำแหน่งปัจจุบัน
print(current_directory)

text_name  = 'folder_list.txt'
# # สร้างไฟล์ .txt และเขียนรายชื่อโฟลเดอร์ลงไป
with open(text_name, 'w', encoding='utf-8') as file:
    for folder in folder_list:
        if os.path.isdir(folder):  # ตรวจสอบว่าเป็นโฟลเดอร์หรือไม่
            file.write(folder + '\n')
