import pandas as pd
import os

# # ในกรณีที่มีไฟล์ CSV
# # df = pd.read_csv('test.csv')

# # ในกรณีที่มีตารางข้อมูลอื่นๆ (ตัวอย่าง: Excel)
# # df = pd.read_excel('test.xlsx')

# # # หรือถ้าต้องการเข้าถึงแถวที่ 1
# # row_1 = df.iloc[0]

# # # แสดงผลลัพธ์
# # print(row_1)


# dataframe = pd.read_excel (r'test.xlsx')
# # col_1_data = dataframe.iloc[:, 0]
# # print(col_1_data)
# row_1_data = dataframe.iloc[0]
# print(row_1_data)
# # print (dataframe)

# สำหรับไฟล์ .xlsx
df_excel_xlsx = pd.read_excel('test.xlsx')

# สำหรับไฟล์ .xls
df_excel_xls = pd.read_excel('test.xls')

# แสดงข้อมูล
# print(df_excel_xlsx)
print(df_excel_xls)