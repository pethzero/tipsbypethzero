import subprocess
from datetime import datetime
# ชื่อโฟลเดอร์ที่ต้องการบีบอัด
folder_name = "exam"

# ระบุที่อยู่ของ WinRAR.exe ในระบบของคุณ
winrar_path = r'C:\Program Files\WinRAR\WinRAR.exe'  # ปรับเป็นที่อยู่ที่ถูกต้องของ WinRAR.exe ในเครื่องคุณ



# ดึงข้อมูลเวลาปัจจุบัน
current_time = datetime.now()
winrar_file_name =  f"{folder_name}_{current_time.strftime('%H_%M_%d_%m_%Y')}.rar"

# เรียกใช้ WinRAR เพื่อทำการบีบอัด
subprocess.run([winrar_path, 'a', '-r',winrar_file_name, folder_name])

# (ตัวเลือก) เปิดโฟลเดอร์ที่บีบอัดด้วยโปรแกรม WinRAR (ถ้ามี WinRAR ติดตั้ง)
# subprocess.Popen(['explorer', f'{folder_name}.rar'])
