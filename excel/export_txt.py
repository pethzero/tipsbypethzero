import pandas as pd

dataframe = pd.read_excel('test.xlsx', header=None)  # กำหนด header=None เพื่อไม่ให้ pandas ใช้แถวแรกเป็นชื่อคอลัมน์

row_1_data = dataframe.iloc[0]

# กำหนดชื่อไฟล์ที่ต้องการเขียน
output_file = 'output.txt'

# ใช้ with open เพื่อเปิดไฟล์และเขียนข้อมูล
with open(output_file, 'w') as file:
    # ใช้ for loop เพื่อเขียนข้อมูลลงไฟล์ทีละบรรทัด
    for value in row_1_data:
        file.write(str(value) + '\n')
