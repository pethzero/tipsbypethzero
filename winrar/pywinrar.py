import os
import subprocess
from datetime import datetime
# ชื่อโฟลเดอร์ที่ต้องการบีบอัด
def compress_folders_with_timestamp(txt_file_path):
    # ระบุที่อยู่ของ WinRAR.exe ในระบบของคุณ
    winrar_path = r'C:\Program Files\WinRAR\WinRAR.exe'  # ปรับเป็นที่อยู่ที่ถูกต้องของ WinRAR.exe ในเครื่องคุณ

    # อ่านไฟล์ txt เพื่อดึงรายชื่อโฟลเดอร์
    with open(txt_file_path, 'r') as file:
        folder_names = [line.strip() for line in file]

    # สร้างไฟล์ zip สำหรับแต่ละโฟลเดอร์
    for folder_name in folder_names:
        if os.path.exists(folder_name) and os.path.isdir(folder_name):
       
            # ดึงข้อมูลเวลาปัจจุบัน
            current_time = datetime.now()
            winrar_file_name =  f"{folder_name}_{current_time.strftime('%H_%M_%d_%m_%Y')}.rar"

            # เรียกใช้ WinRAR เพื่อทำการบีบอัด
            subprocess.run([winrar_path, 'a', '-r',winrar_file_name, folder_name])

# ตัวอย่างการใช้งาน
txt_file_path = '0_folder_names.txt'
compress_folders_with_timestamp(txt_file_path)