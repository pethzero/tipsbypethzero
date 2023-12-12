# อ่านข้อมูลจากไฟล์
with open('empl.sql', 'r') as file:
    sql_data = file.read()

# แสดงข้อมูลที่อ่านได้ (ตรวจสอบเพื่อดูว่าถูกอ่านแล้วถูกต้องหรือไม่)
print(sql_data)

# ปรับปรุงข้อมูล (ตัวอย่าง: เปลี่ยนตัวเลขที่อยู่ที่ตำแหน่งแรกในแต่ละบรรทัดเป็นลำดับตัวเลข)
data_lines = sql_data.split('\n')
modified_data_lines = [tuple([str(index + 1)] + line[1:]) for index, line in enumerate(map(str.strip, data_lines))]

# สร้างข้อมูล SQL ใหม่
new_sql_data = '\n'.join(','.join(line) for line in modified_data_lines)

# แสดงข้อมูล SQL ใหม่ (ตรวจสอบเพื่อดูว่าถูกปรับปรุงถูกต้องหรือไม่)
print(new_sql_data)

# เขียนข้อมูลลงในไฟล์
with open('modified_file.sql', 'w') as file:
    file.write(new_sql_data)
