text = 'ÁÒÊàµÍÃì¿ÍÃìÁÊØ´Ë×è¹'
bytes0 = text.encode('cp1252')
tis_620_text = bytes0.decode('tis-620')
print(text)
print(bytes0)
print(tis_620_text)

# text = 'ÁÒÊàµÍÃì¿ÍÃìÁÊØ´Ë×è¹' # Windows-1252

# # Decode ข้อความใน Windows-1252
# decoded_text = text.encode('Windows-1252').decode('Windows-1252')

# # Encode ข้อความใหม่ใน UTF-8
# utf_8_text = decoded_text.encode('utf-8')

# print(utf_8_text.decode('utf-8'))


text = 'สวัสดีครับ'
bytes_tis620 = text.encode('tis-620', errors='replace')
text_cp1252  = bytes_tis620.decode('cp1252')
text_latin_1 = bytes_tis620.decode('latin-1')
# text_utf_8 = bytes_tis620.decode('utf-8')
print(bytes_tis620)
print(text_cp1252)
print(text_latin_1)
# print(text_utf_8)

#UTF-8 TO TIS-620
# text = 'มาสเตอร์ฟอร์มสุดหื่น'


# Compare
# # สร้างข้อความที่มี Euro Sign (€)
# text_with_euro = "This is a test with Euro Sign (€)"
# # Encode ข้อความใน Latin-1
# encoded_latin1 = text_with_euro.encode('latin-1', errors='replace')
# # Decode ข้อความใน Latin-1
# decoded_latin1 = encoded_latin1.decode('latin-1')


# # Encode ข้อความใน cp1252
# encoded_cp1252 = text_with_euro.encode('cp1252')
# # Decode ข้อความใน cp1252
# decoded_cp1252 = encoded_cp1252.decode('cp1252')
# # เปรียบเทียบข้อความที่ Decode แล้ว

# print("Latin-1 Encode Text:", encoded_latin1)
# print("cp1252 Encode Text:", encoded_cp1252)

# print("Latin-1 Decoded Text:", decoded_latin1)
# print("cp1252 Decoded Text:", decoded_cp1252)

# # เปรียบเทียบข้อความที่มี Euro Sign (€)
# print("Are the decoded texts equal?", decoded_latin1 == decoded_cp1252)


# =========================================================================
# with open('thai_text.txt', 'r', encoding='utf-8') as text_tis620:
#     file_tis620_text = text_tis620.read()
# # # แปลงข้อความจาก tis-620 เป็น bytes ก่อน
# bytes_text = file_tis620_text.encode('tis-620')
# text_latin_1 = bytes_text.decode('latin-1')
# with open('thai_en_de.txt', 'w') as output_file:
#     output_file.write(text_latin_1)
