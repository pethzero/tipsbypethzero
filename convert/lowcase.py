# เปิดไฟล์เพื่ออ่าน
with open('input.txt', 'r') as file:
    # อ่านเนื้อหาของไฟล์
    content = file.read()

# แปลงเป็นตัวเล็ก
lowercase_content = content.lower()

# เปิดไฟล์เพื่อเขียน (สร้างไฟล์ใหม่ถ้ายังไม่มี)
with open('output.txt', 'w') as output_file:
    # เขียนเนื้อหาที่แปลงเป็นตัวเล็กลงไป
    output_file.write(lowercase_content)
