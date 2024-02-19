# เปิดไฟล์เพื่ออ่าน
with open('input.txt', 'r') as file:
    # อ่านเนื้อหาของไฟล์
    content = file.read()

# แปลงเป็นตัวใหญ่
uppercase_content = content.upper()

# เปิดไฟล์เพื่อเขียน (สร้างไฟล์ใหม่ถ้ายังไม่มี)
with open('output.txt', 'w') as output_file:
    # เขียนเนื้อหาที่แปลงเป็นตัวเล็กลงไป
    output_file.write(uppercase_content)
