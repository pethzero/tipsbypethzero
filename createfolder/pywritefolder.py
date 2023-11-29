import os

current_directory = os.getcwd()  # รับตำแหน่งปัจจุบันของ Python
folder_list = os.listdir(current_directory)  # รับรายชื่อไดเรกทอรีในตำแหน่งปัจจุบัน

# สร้างไฟล์ .txt และเขียนรายชื่อโฟลเดอร์ลงไป
with open('folder_list.txt', 'w', encoding='utf-8') as file:
    for folder in folder_list:
        if os.path.isdir(folder):  # ตรวจสอบว่าเป็นโฟลเดอร์หรือไม่
            file.write(folder + '\n')
