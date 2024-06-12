############################ 1. Tuple (()) ############################
# Tuple เป็นโครงสร้างข้อมูลที่คล้ายกับ List แต่มีความแตกต่างตรงที่ Tuple ไม่สามารถเปลี่ยนแปลงค่าได้ (immutable) หลังจากที่สร้างขึ้นมาแล้ว
# สร้าง Tuple ที่เก็บข้อมูลคน
person = ('Alice', 21, 'Computer Science')

# เข้าถึงค่าต่างๆใน Tuple
print(person[0])  # Output: Alice
print(person[1])  # Output: 21
print(person[2])  # Output: Computer Science

# พยายามแก้ไขค่าใน Tuple (จะเกิดข้อผิดพลาด)
# person[1] = 22  # TypeError: 'tuple' object does not support item assignment
############################ 2. Set ({}) ############################
# Set ({})
# Set เป็นโครงสร้างข้อมูลที่เก็บข้อมูลที่ไม่ซ้ำกัน
unique_numbers = {1, 2, 3, 4, 5}

# แสดงข้อมูลใน Set
print("Set:", unique_numbers)


############################ 2. Nested Lists (List within a List) ############################
# Nested Lists (List within a List)
# Nested Lists เป็นโครงสร้างข้อมูลที่ใช้เก็บข้อมูลในรูปแบบของ List ซ้อนกัน
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# แสดงข้อมูลใน Nested Lists
print("Nested Lists:")
for row in matrix:
    print(row)

############################ 3. Nested Lists (List within a List) ############################
# Nested Dictionaries (Dictionary within a Dictionary)
# Nested Dictionaries เป็นโครงสร้างข้อมูลที่ใช้เก็บข้อมูลในรูปแบบของ Dictionary ซ้อนกัน
employee = {'name': 'John', 'details': {'age': 25, 'city': 'New York'}}

# แสดงข้อมูลใน Nested Dictionaries
print("Nested Dictionaries:")
print("Employee:", employee['name'])
print("Details:", employee['details'])

############################ 4. Combination of Data Structures (List with Dictionary as elements) ############################
# Combination of Data Structures (List with Dictionary as elements)
# Combination of Data Structures เป็นโครงสร้างข้อมูลที่ใช้เก็บข้อมูลที่มีโครงสร้างซับซ้อนโดยมีการผสม List และ Dictionary อย่างลึกซึ้งกันเข้าไปใน List หลัก
data = [
    {'name': 'John', 'age': 25, 'friends': ['Jane', 'Bob']},
    {'name': 'Jane', 'age': 30, 'friends': ['John', 'Alice']}
]

# แสดงข้อมูลใน Combination of Data Structures
print("Combination of Data Structures:")
for person in data:
    print("Name:", person['name'])
    print("Age:", person['age'])
    print("Friends:", person['friends'])
