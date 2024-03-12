# data = ['วันที่', 'เลขที่เสนอราคา', 'Rev.', 'รหัสลูกค้า', 'ชื่อเรียก', 'ชื่อลูกค้า', 'ผู้ติดต่อ', 'รายละเอียดสินค้า', 'ชื่อพนักงานขาย', 'เครดิต', 'หมายเหตุ', 'จำนวน', 'หน่วยละ', 'ราคารวม']

# result = {f'head{i+1}': column for i, column in enumerate(data)}

# result_str = "[" + ", ".join([f"'{k}'=> '{v}'" for k, v in result.items()]) + "]"
# print(result_str)

# result_str = "['head'=> " + ", 'head'=> ".join([f"'{value}'" for value in data]) + "]"
# print(result_str)

# result_str = ", ".join([f"['head'=> '{value}']" for value in data])
# print(result_str)

filename_input = 'data_replace_input.txt'
# อ่านข้อมูลจากไฟล์
with open(filename_input, 'r', encoding='utf-8') as input_file:
    data = input_file.read().strip()  # อ่านข้อมูลและลบช่องว่างที่อยู่หน้าหลังข้อความ

# แปลงข้อมูลเป็น list
data_list = eval(data)


print(data_list)
result_str = ", ".join([f"['head'=> '{value}']" for value in data_list])

print(result_str)

filename_output = 'data_replace_output.txt'
# บันทึกข้อมูลกลับไปยังไฟล์
with open(filename_output, 'w', encoding='utf-8') as output_file:
    output_file.write(result_str)