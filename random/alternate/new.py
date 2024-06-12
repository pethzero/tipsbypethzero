import random


# ตัวอย่างข้อมูล
data = [
    {'id': 1, 'item': 'a'},
    {'id': 2, 'item': 'b'},
    {'id': 3, 'item': 'c'},
    {'id': 4, 'item': 'd'},
    {'id': 5, 'item': 'e'},
    {'id': 6, 'item': 'f'},
    {'id': 7, 'item': 'g'},
    {'id': 8, 'item': 'h'},
    {'id': 9, 'item': 'i'},
    {'id': 10, 'item': 'j'}
]


def swap_data(data):
    # สร้างรายการข้อมูลที่สลับแล้ว
    swapped_data = data[:]
    # สลับข้อมูลเป็นคู่ๆ
    for i in range(0, len(swapped_data)-1, 2):
        swapped_data[i], swapped_data[i+1] = swapped_data[i+1], swapped_data[i]
    return swapped_data

def random_swap_data(data):
    # สร้างลิสต์ข้อมูล item
    items = [item['item'] for item in data]

    # สุ่มลำดับของ item แบบไม่ซ้ำกัน
    randomized_items = random.sample(items, len(items))

    # สร้างข้อมูลใหม่โดยใช้ลำดับของ item ที่ถูกสุ่มไว้แล้ว
    randomized_data = [{'id': i + 1, 'item': item} for i, item in enumerate(randomized_items)]
    # # แสดงข้อมูลที่ถูกสุ่มแล้ว
    # for item in randomized_data:
    #     print(item)
    return randomized_data
 
    
# ทดสอบการสลับข้อมูล
# swapped_data = swap_data(data)
# print("Original Data:", data)
# print("Swapped Data:", swapped_data)


random_data = random_swap_data(data)
print("Original Data:", data)
print("Random Swapped Data:", random_data)
