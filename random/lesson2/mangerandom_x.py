import random

data_dulpicate = []

# ตัวอย่างของ data_management เพื่อให้โค้ดสามารถรันได้
data_management = [
    {'id':1,'gender': 'M', 'count': 1, 'plant': 'A', 'exit': 'F'},
    {'id':2,'gender': 'F', 'count': 2, 'plant': 'B', 'exit': 'F'},
    {'id':3,'gender': 'T', 'count': 3, 'plant': 'A', 'exit': 'F'},
    {'id':4,'gender': 'M', 'count': 4, 'plant': 'A', 'exit': 'T'},
]

# ตัวแปรที่ใช้ในการกรอง
gender = 'M'
data_count = 3
plant = 'A'

# กรองข้อมูลตามเงื่อนไขที่กำหนด
filtered_data = [data for data in data_management 
                    if (data['gender'] == 'T' or data['gender'] == gender) 
                        and data['count'] < data_count
                        and data['plant'] == plant
                        and data['exit'] == 'F'
                ]

if filtered_data:
    # เลือกข้อมูลแบบสุ่มจาก filtered_data
    random_data = random.choice(filtered_data)
    data_dulpicate.append(random_data)
    
    # หักลบข้อมูลใน data_management
    data_management.remove(random_data)

print("Random Data:", random_data)
print("Data Dulpicate:", data_dulpicate)
print("Data Management:", data_management)