import shutil

def compress_folder(folder_path, output_path):
    # ให้ output_path รวมถึงชื่อไฟล์และนามสกุลของไฟล์บีบอัด
    shutil.make_archive(output_path, 'zip', folder_path)

# ตัวอย่างการใช้งาน
folder_to_compress = 'exam'
output_archive_name = 'exam_compressed'

compress_folder(folder_to_compress, output_archive_name)
