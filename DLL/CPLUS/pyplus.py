# import platform
# print(platform.architecture())
from ctypes import cdll

# โหลด DLL
result_dll =  cdll.LoadLibrary('.\\mydll64.dll')

# เรียกใช้ฟังก์ชัน helloWorld จาก DLL
result_dll.HelloWorld()

