import ctypes

# โหลด DLL
example_dll = ctypes.CDLL('./ExampleLibrary.dll')

# เรียกใช้ฟังก์ชัน Add
result = example_dll.Add(3, 4)
print(f'Result from DLL: {result}')
