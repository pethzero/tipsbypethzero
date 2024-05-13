import os

def read_folder_pics(file_path):
    group_files = []
    with open(file_path, 'r') as file:
        for line in file:
            group_files.append(line.strip())  # เพิ่มชื่อไฟล์ลงใน list โดยลบช่องว่างหน้าและหลังชื่อไฟล์
    return group_files

def list_folders_and_files(folder_path, file_path, output_file='pic_output.txt'):
    group_files = read_folder_pics(file_path)
    with open(output_file, 'w', encoding='utf-8') as file:
        for root, dirs, files in os.walk(folder_path):
                for file_name in files:
                    file_base, file_extension = os.path.splitext(file_name)
                    file_path = os.path.join(root, file_name)
                    if file_name in group_files:
                        file.write(f"File Data Have ||{file_path}\n")
                    else:
                        if process == 1:
                            file.write(f"Junk Data  ||{file_path}\n")
                        else:
                            os.unlink(file_path)


file_path = "pic_data.txt"
mode = 1
process = 1
if mode == 1:
    current_folder = os.path.join(os.getcwd() , 'pic')
else:
    current_folder = r"D:\TEST\tipsbypethzero\createfolder\process_delete\pic"
    
list_folders_and_files(current_folder, file_path)
