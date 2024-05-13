writefolder.py 
-ค้นหา Folder ใน path ปัจจุบัน แล้วเขียนใส่ใน text_name

createfolder.py
-อ่านไฟล์ text_name แล้ว Create Folder

-deletefolder.py
-อ่านไฟล์ text_name แล้ว Delete Folder


def list_folders(directory):
    return [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]

def delete_folder(folder_path):
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))
    os.rmdir(folder_path)