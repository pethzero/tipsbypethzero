import os
import shutil
from datetime import datetime

def compress_folders_with_timestamp(txt_file_path):
    # อ่านไฟล์ txt เพื่อดึงรายชื่อโฟลเดอร์
    with open(txt_file_path, 'r') as file:
        folder_names = [line.strip() for line in file]

    # สร้างไฟล์ zip สำหรับแต่ละโฟลเดอร์
    for folder_name in folder_names:
        if os.path.exists(folder_name) and os.path.isdir(folder_name):
            # ดึงข้อมูลเวลาปัจจุบัน
            current_time = datetime.now()
            
            # สร้างชื่อไฟล์ zip ในรูปแบบ "exam_hh_mm_dd_MM_yyyy.zip"
            # zip_file_name = f"{folder_name}_{current_time.strftime('%H_%M_%d_%m_%Y')}.zip"
            zip_file_name = f"{folder_name}_{current_time.strftime('%H_%M_%d_%m_%Y')}"
            
            # ทำการบีบอัดโฟลเดอร์
            shutil.make_archive(zip_file_name, 'zip', folder_name)
            print(f"Compressed {folder_name} to {zip_file_name}")

# ตัวอย่างการใช้งาน
txt_file_path = '0_folder_names.txt'
compress_folders_with_timestamp(txt_file_path)
