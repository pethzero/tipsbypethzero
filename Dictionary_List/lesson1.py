############################ 1. Dictionary ({}) ############################
# สร้าง Dictionary ที่เก็บข้อมูลนักเรียน
# Dictionary เป็นโครงสร้างข้อมูลที่เก็บคู่ของคีย์และค่า (key-value pairs) แต่ละคีย์ใน Dictionary ต้องไม่ซ้ำกัน และคีย์สามารถเป็นได้ทั้งสตริง, ตัวเลข, หรือทูเพิลที่ไม่เปลี่ยนแปลง ส่วนค่าของคีย์สามารถเป็นได้ทุกชนิดของข้อมูล


student = {
    'name': 'Alice',
    'age': 21,
    'major': 'Computer Science'
}

# เข้าถึงค่าต่างๆใน Dictionary
print(student['name'])  # Output: Alice
print(student['age'])   # Output: 21
print(student['major']) # Output: Computer Science


############################ 2. List ([]) ############################
# List เป็นโครงสร้างข้อมูลที่เก็บข้อมูลเป็นลำดับ (ordered collection) โดยสามารถเก็บข้อมูลซ้ำได้ และเข้าถึงข้อมูลได้ตามดัชนี (index) โดยดัชนีเริ่มต้นที่ 0
# สร้าง List ที่เก็บผลไม้
fruits = ['apple', 'banana', 'cherry', 'date']

# เข้าถึงค่าต่างๆใน List
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[2])  # Output: cherry
print(fruits[3])  # Output: date

# เพิ่มค่าใน List
fruits.append('elderberry')
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date', 'elderberry']


############################ 3. List of Dictionaries ([{}]) ############################
# สร้าง List of Dictionaries ที่เก็บข้อมูลนักเรียนหลายคน
students = [
    {'name': 'Alice', 'age': 21, 'major': 'Computer Science'},
    {'name': 'Bob', 'age': 22, 'major': 'Mathematics'},
    {'name': 'Charlie', 'age': 23, 'major': 'Physics'}
]

# เข้าถึงค่าต่างๆใน List of Dictionaries
for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Major: {student['major']}")
    
# Output:
# Name: Alice, Age: 21, Major: Computer Science
# Name: Bob, Age: 22, Major: Mathematics
# Name: Charlie, Age: 23, Major: Physics

# สรุปความแตกต่าง
# Dictionary ({}): เป็นการเก็บคู่คีย์และค่า โดยใช้คีย์ในการเข้าถึงค่า
# List ([]): เป็นการเก็บข้อมูลเป็นลำดับ โดยใช้ดัชนีในการเข้าถึงข้อมูล
# List of Dictionaries ([{}]): เป็นการเก็บหลาย Dictionary ในรูปแบบของ List ทำให้สามารถเก็บข้อมูลที่มีโครงสร้างแบบ Dictionary หลายๆ ตัวในลิสต์เดียว
# คุณสามารถเลือกใช้โครงสร้างข้อมูลตามความต้องการของงานที่ต้องการทำได้ครับ/ค่ะ

