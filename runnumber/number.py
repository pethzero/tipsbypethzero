output_filename = 'outputdata.txt'  # ชื่อไฟล์ที่ต้องการสร้างและเขียนข้อมูล
data_to_write = ''  # ข้อความที่ต้องการเขียน
number = 110

with open(output_filename, 'w', encoding='utf-8') as output_file:
    for x in range(number):  # ทำการเขียนข้อมูลซ้ำ 5 ครั้ง
        output_file.write(f"({x},\n")
