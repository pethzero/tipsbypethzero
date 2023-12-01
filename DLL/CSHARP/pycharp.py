# from ctypes import cdll

# # โหลด DLL
# result_dll =  cdll.LoadLibrary('.\\Math1.dll')

# # เรียกใช้ฟังก์ชัน helloWorld จาก DLL
# result_add = result_dll.add(5, 7)
# print("Result from add_numbers DLL:", result_add)


import clr
clr.AddReference("Math1.dll")
from MyMath import Addition

# ใช้คลาส Addition จาก DLL
result = Addition.add(5, 3)

# แสดงผลลัพธ์
print(f"Result: {result}")
