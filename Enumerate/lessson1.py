
############################ 1. การสร้างดัชนีให้กับข้อมูลในลิสต์ ############################
# ข้อมูลตัวอย่าง 
def lesson_1():
    students = ['Alice', 'Bob', 'Charlie', 'David']
    indexed_students = {index: student for index, student in enumerate(students)}
    return indexed_students
# {0: 'Alice', 1: 'Bob', 2: 'Charlie', 3: 'David'}


############################ 2. การแสดงผลข้อมูลพร้อมดัชนี ############################
# ข้อมูลตัวอย่าง
def lesson_2():
    fruits = ['apple', 'banana', 'cherry', 'date']
    results = []
    # แสดงผลข้อมูลพร้อมดัชนี
    for index, fruit in enumerate(fruits):
        print(f"Fruit {index + 1}: {fruit}")
    return "\n".join(results)

############################ 3. การแก้ไขข้อมูลในลิสต์ ############################
# ข้อมูลตัวอย่าง
def lesson_3():
    numbers = [10, 20, 30, 40, 50]

    # แก้ไขข้อมูลในลิสต์
    for index, number in enumerate(numbers):
        if index % 2 == 0:  # แก้ไขข้อมูลที่มีดัชนีเป็นเลขคู่
            numbers[index] = number * 2
    return numbers

############################ 4. การเปรียบเทียบข้อมูลสองลิสต์ ############################
# ข้อมูลตัวอย่าง
def lesson_4():
    list1 = ['a', 'b', 'c', 'd']
    list2 = ['x', 'b', 'y', 'd']
    results = []
    # เปรียบเทียบข้อมูลในสองลิสต์
    for index, (item1, item2) in enumerate(zip(list1, list2)):
        if item1 == item2:
            results.append(f"Match at index {index}: {item1} == {item2}")
        else:
            results.append(f"No match at index {index}: {item1} != {item2}")
    return results


############################ 5. การใช้งานร่วมกับการอ่านไฟล์ ############################
# ข้อมูลตัวอย่างในไฟล์ (สมมุติว่ามีไฟล์ชื่อ 'example.txt' ที่มีเนื้อหาต่อไปนี้)
# Line 1
# Line 2
# Line 3

# อ่านไฟล์และแสดงเลขบรรทัดพร้อมเนื้อหาของแต่ละบรรทัด
def lesson_5():
    results = []
    with open('example.txt', 'r') as file:
        for index, line in enumerate(file):
            results.append(f"Line {index + 1}: {line.strip()}")
    return results



print(lesson_1())
print(lesson_2())
print(lesson_3())
print(lesson_4())
print(lesson_5())