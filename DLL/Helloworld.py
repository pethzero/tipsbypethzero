from ctypes import cdll

# โหลด DLL
EX1_dll =  cdll.LoadLibrary('.\\Helloworld.dll')

# เรียกใช้ฟังก์ชัน helloWorld จาก DLL
EX1_dll.helloWorld()

