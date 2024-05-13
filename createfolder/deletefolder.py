import os
import shutil
text_name  = 'folder_list.txt'
# อ่านรายชื่อโฟลเดอร์จากไฟล์ folder_list.txt
with open(text_name, 'r') as file:
    folder_names = file.read().splitlines()

mode = 2
if mode == 1:
    # ลบโฟลเดอร์ที่ว่างเปล่า
    for folder_name in folder_names:
        if os.path.exists(folder_name) and os.path.isdir(folder_name):
            try:
                # os.rmdir(folder_name)
                #ซึ่งใช้สำหรับการลบไฟล์เท่านั้นและไม่สามารถใช้กับโฟลเดอร์ได้
                os.unlink(folder_name) 
                print(f"Deleted empty folder: {folder_name}")
            except OSError as e:
                print(f"Error: {folder_name} : {e.strerror}")
else:
    # ลบโฟลเดอร์และเนื้อหาภายใน
    for folder_name in folder_names:
        if os.path.exists(folder_name) and os.path.isdir(folder_name):
            try:
                shutil.rmtree(folder_name)
                print(f"Deleted folder and its contents: {folder_name}")
            except OSError as e:
                print(f"Error: {folder_name} : {e.strerror}")