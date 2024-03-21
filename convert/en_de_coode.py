# text = 'ÁÒÊàµÍÃì¿ÍÃìÁÊØ´Ë×è¹'
# bytes0 = text.encode('cp1252')
# text2 = bytes0.decode('tis-620')
# print(text)
# print(bytes0)
# print(text2)
# text = 'มาสเตอร์ฟอร์มสุดหื่น'
# bytes_tis620 = text.encode('tis-620', errors='replace')
# text_cp1252  = bytes_tis620.decode('cp1252')
# text_latin_1 = bytes_tis620.decode('latin-1')
# print(bytes_tis620)
# print(text_cp1252)
# print(text_latin_1)
# =========================================================================
with open('thai_text.txt', 'r', encoding='utf-8') as text_tis620:
    file_tis620_text = text_tis620.read()
# # แปลงข้อความจาก tis-620 เป็น bytes ก่อน
bytes_text = file_tis620_text.encode('tis-620')
text_latin_1 = bytes_text.decode('latin-1')
with open('thai_en_de.txt', 'w') as output_file:
    output_file.write(text_latin_1)
