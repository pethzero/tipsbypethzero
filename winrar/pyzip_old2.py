import os
import shutil

def compress_folders_from_txt(txt_file_path):
    # อ่านไฟล์ txt เพื่อดึงรายชื่อโฟลเดอร์
    with open(txt_file_path, 'r') as file:
        folder_names = [line.strip() for line in file]

    # สร้างไฟล์ zip สำหรับแต่ละโฟลเดอร์
    for folder_name in folder_names:
        if os.path.exists(folder_name) and os.path.isdir(folder_name):
            # ตั้งชื่อไฟล์ zip ในรูปแบบ folder_name.zip
            zip_file_name = f"{folder_name}"
            
            # ทำการบีบอัดโฟลเดอร์
            shutil.make_archive(zip_file_name, 'zip', folder_name)
            print(f"Compressed {folder_name} to {zip_file_name}")

# ตัวอย่างการใช้งาน
txt_file_path = '0_folder_names.txt'
compress_folders_from_txt(txt_file_path)
